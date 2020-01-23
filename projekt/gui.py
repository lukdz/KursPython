import PySimpleGUI as sg
from get import Getter
from gui_list import GuiList

def draw_menu(listbox_pages):
    sg.change_look_and_feel('DefaultNoMoreNagging')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Download list')],
                [sg.Listbox(values=listbox_pages, size=(50, 10), key='_LISTBOX_PAGES_')],
                [sg.Text('Add new page'), 
                sg.InputText(default_text = 'http://google.com', key='_NEW_PAGE_', size=(37, 1))],
                [sg.Button('Ok', bind_return_key=True), sg.Button('Cancel')] ]

    # Create the Window
    return sg.Window('Simple downloader', layout)


listbox_pages = GuiList()
window = draw_menu(listbox_pages.get_iterable())
g = Getter()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=1000)
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        g.close()
        print('Closed')
        break
    if event in 'Ok':
        print('You entered', values['_NEW_PAGE_'])
        counter = listbox_pages.add(values['_NEW_PAGE_'], 'waiting')
        g.put((counter, values['_NEW_PAGE_']))
        values=listbox_pages.get_iterable()
        window.Element('_LISTBOX_PAGES_').Update(values=values,set_to_index=1)
        window.Element('_NEW_PAGE_').Update('')
    # if event == sg.TIMEOUT_KEY:
    #     print("Nothing happened")
    update = g.get()
    if update is not None:
        print('update', update)
        (id, status) = update
        listbox_pages.set_status(id, status)
        values=listbox_pages.get_iterable()
        window.Element('_LISTBOX_PAGES_').Update(values=values,set_to_index=1)
window.close()

