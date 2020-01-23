from db import add_url, list_urls, update_status

class GuiList():
    def __init__(self):
        self.counter = -1
        self.list = list_urls()#[]
        # print( list_urls() )
    def add(self, page, status):
        self.counter += 1
        self.list.append((page, status))
        add_url(page,status)
        return self.counter 
    def set_status(self, id, status):
        (page, _) = self.list[id]
        # update_status(id, status)
        self.list[id] = (page, status)
    def get_iterable(self):
        list_urls()
        return self.list