import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

ranking = [ ['java', 'a', 'ula', 'a'], ['C', 'e', 'ola', 'a'], ['Python', 'b', 'ania', 'a']]
ranking = [ ['java', 'Bill', 'Gates', 'bill@msd.com'], ['Python', 'Steve', 'Jobs', 'steve@mac.com']]

sygnaly = { 'ondestroy': Gtk.main_quit }

builder = Gtk.Builder()
builder.add_from_file('wyklad1.glade')

# model
model = builder.get_object('liststore1')
for p in ranking:
    model.append(p)


# kolumny
view = builder.get_object('treeview1')

r1 = Gtk.CellRendererText()
k1 = Gtk.TreeViewColumn("id", r1, text=0)
k1.set_sizing(Gtk.TreeViewColumnSizing.FIXED)
view.append_column(k1)

r2 = Gtk.CellRendererText()
k2 = Gtk.TreeViewColumn("name", r2, text=1)
k2.set_sizing(Gtk.TreeViewColumnSizing.FIXED)
view.append_column(k2)

r3 = Gtk.CellRendererText()
k3 = Gtk.TreeViewColumn("fullname", r3, text=2)
k3.set_sizing(Gtk.TreeViewColumnSizing.FIXED)
view.append_column(k3)

r3 = Gtk.CellRendererText()
k3 = Gtk.TreeViewColumn("email", r3, text=2)
k3.set_sizing(Gtk.TreeViewColumnSizing.FIXED)
view.append_column(k3)

def on_select(selektor):
    model, treeiter = selektor.get_selected()
    etyk = builder.get_object('label1') 
    if treeiter is not None:
         etyk.set_text("Wybrałeś " + model[treeiter][1])


sel = builder.get_object('treeview-selection1')
sel.connect('changed', on_select)
       
def on_change(selektor):
    model, treeiter = selektor.get_selected()
    etyk = builder.get_object('label1') 
    if treeiter is not None:
         etyk.set_text("Zmieniałeś " + model[treeiter][1])


sel = builder.get_object('liststore1')
sel.connect('row-changed', on_change)

builder.connect_signals(sygnaly)

okno = builder.get_object('okno')

okno.show_all()

Gtk.main()

