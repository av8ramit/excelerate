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

from tkinter import messagebox


sys.path.append('Library')

from Console import *
from Commands import *
from Values import *
c = Console()



#initiate main window
root = Tk()

#set window size
root.geometry("1033x615")

#set window title
root.title("Excelerate")

root.configure(background = 'light steel blue')
#terminal frame
#termframe = Frame(root, height = 400, width = 450)
#termframe.grid(row=7)
#w_id = termframe.winfo_id()
#os.system('konsole -into %d - geometry 400x200 -e /root/.bashrc&' % w_id)

 

####################### Load Images ######################

photo = PhotoImage(file = "./GUI/E.gif")
NUimg = PhotoImage(file = "./GUI/NewStdntButton.gif")
LUimg = PhotoImage(file = "./GUI/LoadStdntButton.gif")
Gimg = PhotoImage(file = "./GUI/GradeButton.gif")
CASimg = PhotoImage(file = "./GUI/CreateAnsButton.gif")
Rptimg = PhotoImage(file = "./GUI/ReportsButton.gif")
Rstimg = PhotoImage(file = "./GUI/ResetButton.gif")
Svimg = PhotoImage(file = "./GUI/SaveButton.gif")
AutoGrdr = PhotoImage(file = "./GUI/AutoGrdr.gif")


################### Functions ##########################

def save_user():
    res = c.process_commands('save')
    if (not res):
            messagebox.showwarning("Error", c.error)

def reset_user():
    res = c.process_commands('reset')   
    if (not res):
            messagebox.showwarning("Error", c.error) 

def delete_user():
    res = c.process_commands('delete_student')
    if (not res):
            messagebox.showwarning("Error", c.error)
def simple_report():
    res = c.process_commands('simple_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:     
        name = c.user.name 
        dirc = user_directory(name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'simple_report.html' ) 
def advance_report():
    res = c.process_commands('advanced_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:     
        name = c.user.name 
        dirc = user_directory(name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'advanced_report.html' )
def graph_report():
    res = c.process_commands('graph_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:     
        name = c.user.name 
        dirc = user_directory(name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'graph_report.html' )
def section_report():
    res = c.process_commands('section_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:    
        name = c.user.name 
        dirc = user_directory(name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'math_report.html' )
            os.system('open ' + dirc + DIR_SEP + 'reading_report.html' )
            os.system('open ' + dirc + DIR_SEP + 'writing_report.html' )

def get_new_user():
    name = tkinter.simpledialog.askstring( 'New Student', 'Enter New Username')
    if(name != None):
        res = c.process_commands('new_student ' + name)
        if (not res):
            messagebox.showwarning("Error", c.error)
        else:     
            var = StringVar()
            if(c.state == LOAD_STATE):
                UserName = c.user.name
                var.set(UserName)
                if(UserName != None):
                    cu.grid_forget
                    nm.gird_forget
                    cu = Label(root, text = 'Current Student:', pady = 2, background = 'steel blue')
                    nm = Label(root, textvariable =  var, pady = 2, background = 'steel blue')
                    cu.grid(row = 0, column = 0, sticky = E)
                    nm.grid(row = 0, column = 1, sticky = (W))
def get_load_user():
    name = tkinter.simpledialog.askstring( 'Load Student', 'Enter Username')
    if(name != None):
        res = c.process_commands('load_student ' + name)
        if (not res):
            messagebox.showwarning("Error", c.error)
     
        else:    
            var = StringVar()
            if(c.state == LOAD_STATE):
                UserName = c.user.name 
                var.set(UserName)
                if(UserName != None):
                    cu = Label(root, text = 'Current Student:', pady = 1, background = 'steel blue')
                    nm = Label(root, textvariable =  var, pady = 1, background = 'steel blue')
                    cu.grid_forget()
                    nm.grid_forget()   
                    cu.grid(row = 0, column = 0, sticky = E)
                    nm.grid(row = 0 , column= 1, sticky = (W))

def get_test_name():
   
     if(c.user is not None):
        file_path = tkinter.filedialog.askopenfilename( initialdir = './Users' + DIR_SEP + c.user.name )
        if (not file_path):
            return
        #extract filename from pathing stored in file_path
        file_name = os.path.basename(file_path)
        if (file_name != None):
            res = c.process_commands('grade ' + file_name)
            if (not res):
                messagebox.showwarning("Error", c.error)
            else:
                name = c.user.name 
                dirc = user_directory(name) 
                fname = os.path.basename(dirc)
                if (dirc != None):
                    os.system('open ' + dirc + DIR_SEP + 'grade.html' )     
     else:
        messagebox.showwarning("Error", 'Please Load Or Create A Student First')           

def get_test_id():
    if(c.user is not None):
        name = tkinter.simpledialog.askstring( 'Create Answer Sheet', 'Enter Test ID')
        if(name != None):
            res = c.process_commands('answer_sheet ' + name)
            if (not res):
                messagebox.showwarning("Error", c.error)
    else:
        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 


######################################################################

#prevent menu items from being taken off the window
root.option_add('*tearOff', FALSE)


################ Menu ##############
menubar = Menu(root)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menu_view = Menu(menubar)
menu_help = Menu(menubar)
menubar.add_cascade(menu = menu_file, label = 'File')
menubar.add_cascade(menu = menu_edit, label = 'Edit')
menubar.add_cascade(menu = menu_view, label = 'View')
menubar.add_cascade(menu = menu_help, label = 'Help')


menu_file.add_command(label='New User', command = get_new_user)
menu_file.add_command(label = 'Load User', command = get_load_user)
menu_file.add_command(label = 'Save', command = save_user)
menu_view.add_command(label= 'Grade A Test', command = get_test_name)
menu_file.add_command(label = 'Reset Tests', command = reset_user)

menu_view.add_command(label = 'Create Answer Sheet', command = get_test_id)
menu_view.add_command(label = 'Open Simple Report', command = simple_report)
menu_view.add_command(label = 'Open Advanced Report', command = advance_report)
menu_view.add_command(label = 'Open Section Reports', command = section_report)
menu_view.add_command(label = 'Open Graph Report', command = graph_report)

menu_help.add_command(label = 'FAQ') # , command = )
menu_help.add_command(label = 'Usage') #   , command = )
#display the menu
root.config(menu=menubar)
#######################################


# Logo
Label(root, image = photo, background = 'light steel blue').grid(row=0, column = 2, columnspan = 3) 


####### MAIN COLORED GUI BUTTONS 

Button( root, image = NUimg, width = 250, height = 250, pady = 0,  command= get_new_user).grid( row = 1, column = 0 ,columnspan = 2, rowspan = 2, sticky = (W))

Button( root, image = LUimg , width = 250, height = 250, pady = 0, command = get_load_user).grid(row = 1, column = 2, columnspan = 2, rowspan = 2,sticky = W)


Button( root, image = Gimg, width = 250, height = 250,  pady = 0,  command = get_test_name ).grid( row = 1,column = 10, columnspan = 2, rowspan = 2,sticky = W)
 

Button( root, image = CASimg,  width = 250, height = 250, pady = 0 , command = get_test_id).grid( row = 1, column = 4, columnspan = 2, rowspan = 2,sticky = W)

Button( root, image = Rstimg,  width = 250, height = 250, pady = 0, command = reset_user).grid( row = 9, column = 9, columnspan = 2, rowspan = 2,sticky = W)

Button( root, image = Svimg,  width = 250, height = 250, pady = 0, command = save_user ).grid( row = 10, column = 2, columnspan = 2, rowspan = 2,sticky = W)

Button( root, image = AutoGrdr,  width = 250, height = 250, pady = 0).grid( row = 10, column = 4, columnspan = 2, rowspan = 2,sticky = W)

## Reports Submenu Button

mb = Menubutton( root, image = Rptimg, width = 254, height = 255)
mb.grid(row = 10, column = 0, columnspan = 3, rowspan = 2, sticky = (W))
mb.menu = Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_checkbutton(label = "Simple Report", command = simple_report)
mb.menu.add_checkbutton(label ="Advanced Report", command = advance_report)
mb.menu.add_checkbutton(label ="Graphs Report", command = graph_report)
mb.menu.add_checkbutton(label ="Section Report", command = section_report)


# Tk enters its event loop
root.mainloop()


