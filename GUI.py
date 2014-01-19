#!/usr/bin/python


# import tkinter, load existing TK library on system
from tkinter import *
# import python's binding to newer "themed widgets" added to Tk in 8.5
from tkinter import ttk
#import prompt messages
import tkinter.simpledialog
#import os to spawn tty inside frame
import os
#import filedialog for load_user/save
import tkinter.filedialog

import sys

#import image format support
#from PIL import Image, ImageTk

sys.path.append('Library')

from Console import *
from Commands import *
from Values import *
c = Console()

#initiate main window
root = Tk()

#set window size
root.geometry("570x700")

#set window title
root.title("Excelerate")

root.configure(background = 'powder blue')
#terminal frame
#termframe = Frame(root, height = 400, width = 450)
#termframe.grid(row=7)
#w_id = termframe.winfo_id()
#os.system('konsole -into %d - geometry 400x200 -e /root/.bashrc&' % w_id)

### Display Logo

photo = PhotoImage(file = "./GUI/logo.ppm")




# data capture functions; *name* to be passed to console functions

def simple_report():
    c.process_commands('simple_report')
    name = c.user.name 
    dirc = user_directory(name) 
    fname = os.path.basename(dirc)
    if (dirc != None):
        os.system('open ' + dirc + DIR_SEP + 'simple_report.html' ) 
def advance_report():
    c.process_commands('advanced_report')
    name = c.user.name 
    dirc = user_directory(name) 
    fname = os.path.basename(dirc)
    if (dirc != None):
        os.system('open ' + dirc + DIR_SEP + 'advanced_report.html' )
def graph_report():
    c.process_commands('graph_report')
    name = c.user.name 
    dirc = user_directory(name) 
    fname = os.path.basename(dirc)
    if (dirc != None):
        os.system('open ' + dirc + DIR_SEP + 'graph_report.html' )
def section_report():
    c.process_commands('section_report')
    name = c.user.name 
    dirc = user_directory(name) 
    fname = os.path.basename(dirc)
    if (dirc != None):
        os.system('open ' + dirc + DIR_SEP + 'math_report.html' )
        os.system('open ' + dirc + DIR_SEP + 'reading_report.html' )
        os.system('open ' + dirc + DIR_SEP + 'writing_report.html' )

def get_new_user():
    name = tkinter.simpledialog.askstring( 'New User', 'Enter New Username')
    if(name != None):
        c.process_commands('new_user ' + name)
        # option below opens new user's folder       
        file_name = tkinter.filedialog.askopenfilename( initialdir = './Users' + DIR_SEP + name)
        os.system('open ' + file_name)
def get_load_user():
    name = tkinter.simpledialog.askstring( 'Load User', 'Enter Username')
    if(name != None):
        c.process_commands('load_user ' + name)
         # option below opens loaded user's folder       
        #file_name = tkinter.filedialog.askopenfilename( initialdir = './Users' + '/' + name)
        #if(file_name != None):
        #    os.system('open ' + file_name)
def get_test_name():
    #name = tkinter.simpledialog.askstring( 'Grade Test', 'Enter Filename To Grade')
    #if(name != None):
        #test = tkinter.filedialog.askopenfilename( initialdir = './Users' + '/' + name)
    
    file_path = tkinter.filedialog.askopenfilename( initialdir = './Users' )
    #extract filename from pathing stored in file_path
    file_name = os.path.basename(file_path)
    if (file_name != None):
        c.process_commands('grade ' + file_name)
def get_test_id():
    name = tkinter.simpledialog.askstring( 'Create Answer Sheet', 'Enter Test ID')
    if(name != None):
        c.process_commands('answer_sheet ' + name)


#prevent menu items from being taken off the window
root.option_add('*tearOff', FALSE)

# main frame that will hold all the widgets
#mainframe = Frame( root, relief = SUNKEN)

#set up grid structure in main frame - sticky options for more precise widget placement
#mainframe.grid(column = 0, row = 0, sticky =(N, W, E, S))

# row and column expansion if main window is resized
#mainframe.rowconfigure(0, weight = 1)
#mainframe.columnconfigure(0, weight = 1)


#### Menu


menubar = Menu(root)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menu_view = Menu(menubar)
menubar.add_cascade(menu = menu_file, label = 'File')
menubar.add_cascade(menu = menu_edit, label = 'Edit')
menubar.add_cascade(menu = menu_view, label = 'View')



menu_file.add_command(label='New User', command = get_new_user)
menu_file.add_command(label = 'Load User', command = get_load_user)
menu_file.add_command(label = 'Save')
menu_view.add_command(label= 'Grade A Test', command = get_test_name)
menu_file.add_command(label = 'Reset Tests')

menu_view.add_command(label = 'Create Answer Sheet', command = get_test_id)
menu_view.add_command(label = 'Print Simple Report')
menu_view.add_command(label = 'Print Detailed Report')
#display the menu
root.config(menu=menubar)


#buttons w/ user entry
#nw_usr = LabelFrame(root, text = "New User", padx = 5, pady = 5)#grid(column = 2, row = 2, sticky=(W,E))

Label(root, image = photo, pady= 5).grid(row=0)#, rowspan = 5)


#Label(root, text = "New User:", pady = 5, background = "LightSkyBlue2").grid(row=10, sticky = W)
#separator1 = Frame(root, height=1, bd=1, relief=SUNKEN).grid(row = 1, columnspan = 2)
#Label(root, text = "Load User:", pady = 5, background = "LightSkyBlue3").grid(row = 12, sticky = W)
 
#separator2 = Frame(root, height=1, bd=1, relief=SUNKEN).grid(row = 3, columnspan = 2)
#Label(root, text = "Grade Test:",  pady = 5, background = "LightSkyBlue1").grid(row = 14, sticky =W)
 
#separator3 = Frame(root, height=1, bd=1, relief=SUNKEN).grid(row = 5, columnspan = 2)
#Label(root, text = "Create Answer Sheet:", pady = 5, background = "LightSkyBlue4").grid(row = 16, sticky =W)


#entry = Entry(root) 
#entry.grid(row = 0, column = 1)

group = LabelFrame(root, text="Menu", padx = 5, pady = 5, width = 200, height = 300, background='cadet blue')#, rowspan = 20, columnspan = 5)

group.grid(column = 0)

Button( group , text = "Create New User", pady = 0,  foreground = "red", command= get_new_user).grid( row = 1, columnspan = 3, rowspan = 2, sticky = (W))

Button( group, text = "Load User", pady = 0, foreground = 'SteelBlue2', command = get_load_user).grid(row = 5, columnspan = 3, rowspan = 2,sticky = W)


Button( group, text = "Grade Tests",  pady = 0,  foreground = 'SteelBlue3', command = get_test_name ).grid( row = 10,columnspan = 3, rowspan = 2,sticky = W)
 

Button( group, text = "Create Answer Sheet", pady = 0,  foreground = 'SteelBlue4', command = get_test_id).grid( row = 15,columnspan = 3, rowspan = 2,sticky = W)

mb = Menubutton( group, text = "Reports", relief = SUNKEN )
mb.grid(row = 20, columnspan = 3, rowspan = 10, sticky = (W,E))
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_checkbutton(label = "Simple Report", command = simple_report)
mb.menu.add_checkbutton(label ="Advanced Report", command = advance_report)
mb.menu.add_checkbutton(label ="Graphs Report", command = graph_report)
mb.menu.add_checkbutton(label ="Section Report", command = section_report)
#for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)

# Tk enters its event loop
root.mainloop()


