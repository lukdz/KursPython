import PySimpleGUI as sg
from db import Database

sg.change_look_and_feel('DefaultNoMoreNagging')    # Add a touch of color

def draw_window(title, headings, ranking, new_rows, buttons):
    header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]

    input_rows = [[sg.InputText(col, size=(15,1), pad=(0,0)) for col in row] for row in ranking]
    input_rows += new_rows

    layout = header + input_rows + buttons

    return sg.Window(title, layout, font='Courier 12')

def draw_window_book(ranking):
    title = 'Books'
    headings = ['id', 'title', 'author', 'year', 'holder']
    new_rows = [
        [sg.Text('New book', size=(15,1), pad=(0,0))]
        + [sg.InputText('', size=(15,1), pad=(0,0)) for col in range(len(headings)-2)]
               ]
    buttons = [[sg.Button('Users'), sg.Button('Add book'), sg.Button('Save books')]]
    return draw_window(title, headings, ranking, new_rows, buttons)

def draw_window_user(ranking):
    title = 'Users'
    headings = ['id', 'name', 'fullname', 'email']
    new_rows = [
        [sg.Text('New user', size=(15,1), pad=(0,0))]
        + [sg.InputText('', size=(15,1), pad=(0,0)) for col in range(len(headings)-1)]
               ]
    buttons = [[sg.Button('Books'), sg.Button('Add user')]]#, sg.Button('Save users')]]
    return draw_window(title, headings, ranking, new_rows, buttons)

def get_books(db):
    return [x.to_list() for x in db.list_books()] 

def get_users(db):
    return [x.to_list() for x in db.list_users()] 

def save_users(db, values):
    print( 'save_users' )
    length = 4
    gui = [ values[j] for j in range(len(values)//length*length, len(values)) ]
    if gui != ['', '', '']:
        print( 'Adding ', gui)
        db.add_user(gui[0], gui[1], gui[2])

def save_books(db, values):
    print( 'save_books' )
    length = 5
    db_books = get_books(db)
    for i in range(len(values)//length):
        gui = [ values[i*length+j] for j in range(length) ]
        if gui[4] != str(db_books[i][4]):
            if gui[4] == '':
                print( 'Back ')
                db.back(gui[1], '')
            elif gui[4] != 'None':
                print( 'borrow ')
                db.borrow(gui[1], gui[4])

db = Database()
ranking = get_books(db)
window = draw_window_book(ranking)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event == 'Books':
        window1 = draw_window_book(get_books(db))
        ranking = get_books(db)
        window.Close()
        window = window1
    if event == 'Users':
        ranking = get_users(db)
        window1 = draw_window_user(ranking)
        window.Close()
        window = window1
    if event == 'Add user':
        l = len(values)
        db.add_user(values[l-3], values[l-2], values[l-1])
        ranking = get_users(db)
        window1 = draw_window_user(ranking)
        window.Close()
        window = window1
    if event == 'Add book':
        l = len(values)
        db.add_book(values[l-3], values[l-2], values[l-1])
        ranking = get_books(db)
        window1 = draw_window_book(ranking)
        window.Close()
        window = window1
    if event == 'Save user':
        save_users(db, values)
    if event == 'Save books':
        save_books(db, values)
        ranking = get_books(db)
        window1 = draw_window_book(ranking)
        window.Close()
        window = window1



