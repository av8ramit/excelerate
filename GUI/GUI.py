#!/usr/bin/python


#function that requests new user name

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

sys.path.append('../Library')

from Console import *
from Commands import *
from Values import *
c = Console()

#initiate main window
root = Tk()

#set window size
root.geometry("700x700")

#set window title
root.title("Excelerate")

#terminal frame
#termframe = Frame(root, height = 400, width = 450)
#termframe.grid(row=7)
#w_id = termframe.winfo_id()
#os.system('konsole -into %d - geometry 400x200 -e /root/.bashrc&' % w_id)

# data capture functions; *name* to be passed to console functions
def get_new_user():
    name = tkinter.simpledialog.askstring( 'New User', 'Enter New Username')
    c.process_commands('new_user ' + name)

def get_load_user():
    name = tkinter.simpledialog.askstring( 'Load User', 'Enter Username')
    print(name)
def get_test_name():
    name = tkinter.simpledialog.askstring( 'Grade Test', 'Enter Filename To Grade')
    print(name)

def get_test_id():
    name = tkinter.simpledialog.askstring( 'Create Answer Sheet', 'Enter Test ID')
    print(name)

def open_file ():
    name = tkinter.filedialog.askopenfilename( initialdir = '../Library' )
   # print(name)

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

Label(root, text = "New User:").grid(row=0, sticky = W)
Label(root, text = "Load User:").grid(row = 2, sticky = W)
Label(root, text = "Grade Test:").grid(row = 4, sticky =W)
Label(root, text = "Create Answer Sheet:").grid(row = 6, sticky =W)
#entry = Entry(root) 
#entry.grid(row = 0, column = 1)

Button( root , text = "Create", command= get_new_user).grid(column = 1, row = 0, sticky = (W))
Button( root, text = "Load", command = get_load_user).grid(column = 1, row = 2, sticky = W)
Button( root, text = "Grade", command = get_test_name ).grid(column = 1, row = 4, sticky = W)
Button( root, text = "Create", command = get_test_id).grid(column = 1, row = 6, sticky = W)
#for child in root.winfo_children(): child.grid_configure(padx=5, pady=5)

# Tk enters its event loop
root.mainloop()


