import gtk
import geany
import pygtk
from multisearch import MultiTermSearch

class Analyzer(geany.Plugin):

    __plugin_name__ = "MultiTerm Search"
    __plugin_version__ = "1.0"
    __plugin_description__ = "Search for multiple terms at once in a file"
    __plugin_author__ = "/,David Green crokett@gmail.com>"

    def __init__(self):
        self.menu_item = gtk.MenuItem("Analyzer")
        self.menu_item.show()
        geany.main_widgets.tools_menu.append(self.menu_item)
        self.menu_item.connect("activate", self.on_hello_item_clicked)

    def cleanup(self):
        self.menu_item.destroy()

    def on_hello_item_clicked(widget, data):
        # geany.dialogs.show_msgbox("It Works")
        newwindow = MultiTermSearch()


 
