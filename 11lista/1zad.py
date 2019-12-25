import PySimpleGUI as sg
from db import Database

def draw_window(books, users):
    sg.change_look_and_feel('DefaultNoMoreNagging')   # Add no color

    tab1_layout = [ [sg.Listbox(values=books, size=(30, 6), key='_LISTBOX_BOOKS_')],
                    [sg.Button('Add book'), sg.Button('Edit book')] ]

    tab2_layout = [ [sg.Listbox(values=users, size=(30, 6), key='_LISTBOX_USERS_')],
                    [sg.Button('Add user'), sg.Button('Edit user')] ]

    layout = [[sg.TabGroup([[sg.Tab('Books', tab1_layout), sg.Tab('Users', tab2_layout)]])]]

    return sg.Window('Library Manager', layout)

def new_book(db):
    layout = [  [sg.Text('Title'), sg.InputText()],
                [sg.Text('Author'), sg.InputText()],
                [sg.Text('Year'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('New book', layout)

    event, values = window.read()
    if event == 'Ok':
        db.add_book(values[0], values[1], values[2])
    window.close()

def edit_book(db, book):
    if book[4] is None:
        default_value = ''
    else:
        default_value = get_users(db)[book[4]-1]
    layout = [  [sg.Text('Title'), sg.InputText(book[1])],
                [sg.Text('Author'), sg.InputText(book[2])],
                [sg.Text('Year'), sg.InputText(book[3])],
                [sg.Text('Holder'), sg.Combo(get_users(db), default_value=default_value)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Edit book', layout)

    event, values = window.read()
    if event == 'Ok':
        db.edit_book(book[0], values[0], values[1], values[2], values[3][0])
    window.close()

def new_user(db):
    layout = [  [sg.Text('Name'), sg.InputText()],
                [sg.Text('Fullname'), sg.InputText()],
                [sg.Text('E-mail'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('New book', layout)

    event, values = window.read()
    if event == 'Ok': 
        db.add_user(values[0], values[1], values[2])
    window.close()

def edit_user(db, user):
    layout = [  [sg.Text('Name'), sg.InputText(user[1])],
                [sg.Text('Fullname'), sg.InputText(user[2])],
                [sg.Text('E-mail'), sg.InputText(user[3])],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Edit book', layout)

    event, values = window.read()
    if event is 'Ok':
        db.edit_user(user[0], values[0], values[1], values[2])
    window.close()

def get_books(db):
    return [x.to_list() for x in db.list_books()] 

def get_users(db):
    return [x.to_list() for x in db.list_users()] 

db = Database()
window = draw_window(get_books(db), get_users(db))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event == 'Add book':   
        new_book(db)
        window.Element('_LISTBOX_BOOKS_').Update(values=get_books(db))
    if event == 'Edit book':   
        edit_book(db, values['_LISTBOX_BOOKS_'][0])
        window.Element('_LISTBOX_BOOKS_').Update(values=get_books(db))
    if event == 'Add user':   
        new_user(db)
        window.Element('_LISTBOX_USERS_').Update(values=get_users(db))
    if event == 'Edit user':   
        edit_user(db, values['_LISTBOX_USERS_'][0])
        window.Element('_LISTBOX_USERS_').Update(values=get_users(db))
    print('Library Manager ', values)

window.close()