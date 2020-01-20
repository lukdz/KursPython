import PySimpleGUI as sg
from get import Getter

def draw_menu():
    sg.change_look_and_feel('DefaultNoMoreNagging')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Download list')],
                [sg.Listbox(values=[], size=(30, 10), key='_LISTBOX_PAGES_')],
                [sg.Text('Add new page'), sg.InputText(key='_NEW_PAGE_')],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    return sg.Window('Simple downloader', layout)

window = draw_menu()
listbox_pages = []
g = Getter()


class Kolejka():
    def __init__(self):
        self.counter = 0
        self.list = []
    def add(self, page, status):
        self.counter += 1
        self.list.append((page, status))
        return self.counter 
    def set_status(self, id, status):
        (page, _) = self.list[id]
        self.list[id] = (page, status)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=1000)
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        g.close()
        print('Closed')
        break
    if event in 'Ok':
        g.put(values['_NEW_PAGE_'])
        print('You entered', values['_NEW_PAGE_'])
        listbox_pages.append((values['_NEW_PAGE_'], 'waiting'))
        window.Element('_LISTBOX_PAGES_').Update(values=listbox_pages,set_to_index=1)
        window.Element('_NEW_PAGE_').Update('')
    # if event == sg.TIMEOUT_KEY:
    #     print("Nothing happened")
    update = g.get()
    if update is not None:
        print('update', update)
window.close()


##################