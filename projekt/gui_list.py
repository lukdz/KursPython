from db import add_url, list_urls, update_status

class GuiList():
    def __init__(self):
        self.list = list_urls()
    def add(self, page, status):
        return add_url(page,status)
    def set_status(self, id, status):
        update_status(id, status)
    def get_iterable(self):
        return list_urls()