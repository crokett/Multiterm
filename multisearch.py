#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

#gtk.Notebook
#Find_In_Files

'''

GtkWidget *editor_menu - gtk.Menu
GtkWidget *message_window_notebook - gtk.Notebook
GtkWidget *notebook - gtk.Notebook
GtkWidget *progressbar - gtk.ProgressBar
GtkWidget *project_menu - gtk.Menu
GtkWidget *sidebar_notebook - gtk.Notebook
GtkWidget *toolbar - gtk.Toolbar
GtkWidget *tools_menu - gtk.Menu
GtkWidget *window - gtk.Window 
'''
        
class MultiTermSearch:
	    
    global builder 
    global filechooser
    global liststore
        
    def __init__(self):
        print("running")
		#set the glade file
        self.gladefile = "/home/crokett/Data/Projects/Glade/MultiTerm2.glade"
        print("Gladefile is: self.gladefile")
        #self.wTree = gtk.glade.XML(self.gladefile)
        # try gtk file
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
       
        #placeholder widget
        button = self.builder.get_object("loadButton")
        arrow = self.builder.get_object("addButton")
        
        arrow.connect("button-press-event", self.on_arrowButton_clicked)
        self.liststore=self.builder.get_object("searchTermsListStore")
        
        #Get the Main Window, and connect the "destroy" event
        self.window = self.builder.get_object("mainWindow")
       
        
        if (self.window):
           print("Found main window")
           print self.window.get_title()
           self.window.connect("destroy", gtk.main_quit)
           self.window.show()
           
    def on_arrowButton_clicked(self, button):
           print("arrow button clicked")
     
    def on_loadButton_clicked(self, button):
        # builder = gtk.Builder()
       #  builder.add_from_file(self.gladefile)
        # builder.connect_signals(self)
         self.filechooser = self.builder.get_object("fileChooser")
         #self.filechooser.set_default_response(gtk.RESPONSE_OK)
         self.filechooser.show()
         response = self.filechooser.run()
         
    def on_fileChooserOpen_clicked(self, button):
        
        titer = gtk.TreeIter
        # filename = self.filechooser.get_filename()
        filename = "/home/crokett/Data/Projects/Python/terms.txt"
        termsfile = open(filename, 'r')
        
        for line in termsfile:
			#add line to the list store
            iter = self.liststore.append()
            self.liststore.set(iter, 0, line)
			
			#this line gives error on invalid length when uncommented
          #liststore.append(line)
        self.filechooser.hide()
    
    def on_fileChooserCancel_clicked(self, button):
        self.filechooser = self.builder.get_object("fileChooser")
        print("cancel clicked")
        self.filechooser.hide()
		
    def on_searchTermArrow_press(self, arrow):
        texttoadd = self.builder.get_object("searchTermsTextEntry").get_text()       
        print("arrow clicked")
        print(texttoadd)
        iter = self.liststore.append()
        self.liststore.set(iter, 0, texttoadd)
        

    def on_saveButton_clicked(self, button):
        chooser = gtk.FileChooserDialog(title=None,action=gtk.FILE_CHOOSER_ACTION_SAVE,
                 buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        filename = chooser.get_filename()
        termsfile = open(filename, 'w')
        liststore = self.builder.get_object("searchTermsListStore")
        for row in liststore:
            termsfile.write(row)
          
        
        
        
		
           
if __name__ == "__main__":
           print("main found")
           mts = MultiTermSearch()
           gtk.main()
         
       
