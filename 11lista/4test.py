import PySimpleGUI as sg
from db import Database

def draw_window(title, headings, ranking, buttons):
    sg.change_look_and_feel('DefaultNoMoreNagging')    # Add a touch of color

    header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]

    input_rows = [[sg.InputText(col, size=(15,1), pad=(0,0)) for col in row] for row in ranking]

    layout = header + input_rows + buttons

    return sg.Window(title, layout, font='Courier 12')

def draw_window_book(ranking):
    title = 'Books'
    headings = ['id', 'title', 'author', 'year', 'holder']
    buttons = [[sg.Button('Users'), sg.Button('Add book')]]
    return draw_window(title, headings, ranking, buttons)

def draw_window_user(ranking):
    title = 'Users'
    headings = ['id', 'name', 'fullname', 'email']
    buttons = [[sg.Button('Books'), sg.Button('Add user')]]
    return draw_window(title, headings, ranking, buttons)

def get_books(db):
    return [x.to_list() for x in db.list_books()] 

def get_users(db):
    return [x.to_list() for x in db.list_users()] 


db = Database()
ranking = get_books(db)
window = draw_window_book(ranking)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event == 'Books':
        window1 = draw_window_book(get_books(db))
        window.Close()
        window = window1
        print('Books ', values[0])
    if event == 'Users':
        print( get_users(db) )
        window1 = draw_window_user(get_users(db))
        window.Close()
        window = window1
        print('Users ', values[0])
    if event == 'Add user':
        ranking = get_users(db)
        ranking += [ ['', '', '', ''] ]
        window1 = draw_window_book(ranking)
        window.Close()
        window = window1
        print('Add user ', values[0])
