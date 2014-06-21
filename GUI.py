#!/usr/bin/python




####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been created by Neel Bhadra:                                                                                                   #
#     Created by              : neel.bhadra                                                                                                      #    
#     Created on              : 12-26-2013                                                                                                         #
#     Directory               : /Excelerate/                                                                                                          #
#     Purpose                 : This file creates and launches our Graphical User Interface                                                                                 #
#                                                                                                                                                  #
#################################################################################################################################################### 


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
from Graph import *
import csv
from Summary import *
from User import *
c = Console()



#initiate main window
root = Tk()

#set window size
root.geometry("1280x633")

#set window title
root.title("Excelerate")

root.configure(background = 'light steel blue')
#terminal frame
#termframe = Frame(root, height = 400, width = 450)
#termframe.grid(row=7)
#w_id = termframe.winfo_id()
#os.system('konsole -into %d - geometry 400x200 -e /root/.bashrc&' % w_id)


status = Label(root, text="(c) 2014 Excelerate Test Prep", bd=2, relief=SUNKEN)
status.grid(row = 50, column = 4)
## window for NEW/LOAD class 
win = Toplevel(root)
win.geometry("510x260+410+240")
win.title("Excelerate")
win.configure(background = 'light steel blue')
win.lift(root)
####################### Load Images for buttons ######################

photo = PhotoImage(file = "./GUI/E.gif")
NUimg = PhotoImage(file = "./GUI/NewStdntButton.gif")
LUimg = PhotoImage(file = "./GUI/LoadStdntButton.gif")
Gimg = PhotoImage(file = "./GUI/GradeButton.gif")
CASimg = PhotoImage(file = "./GUI/CreateAnsButton.gif")
Rptimg = PhotoImage(file = "./GUI/ReportsButton.gif")
Rstimg = PhotoImage(file = "./GUI/ResetButton.gif")
Svimg = PhotoImage(file = "./GUI/SaveButton.gif")
AutoGrdr = PhotoImage(file = "./GUI/AutoGrdr.gif")
GoalSchl = PhotoImage(file = "./GUI/GoalSchool.gif")
ClassAnly = PhotoImage(file = "./GUI/CollegeA.gif")
LoadClass = PhotoImage(file = "./GUI/LdCls.gif")
NewClass = PhotoImage(file = "./GUI/NwCls.gif")
ChngClass = PhotoImage(file = "./GUI/ChCls.gif")
################### Functions ##########################
def help_usage():
    os.system('open ' + './Documents/Usage_v1.pdf' )

def save_user():
    res = c.process_commands('save')
    if (not res):
            messagebox.showwarning("Error", c.error)

def reset_user():
    ans = messagebox.askyesno('Reset User', 'Are you sure you want to reset user? This will permanently remove all data and history.')
    if( ans is True):

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
        dirc = user_directory(name, c.c.name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'simple_report.html' ) 
def advance_report():
    res = c.process_commands('advanced_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:     
        name = c.user.name 
        dirc = user_directory(name, c.c.name) 
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'advanced_report.html' )
def graph_report():
    res = c.process_commands('graph_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:     
        name = c.user.name 
        dirc = user_directory(name, c.c.name) #passing user name and console's class object's name attribute
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'graph_report.html' )
def section_report():
    res = c.process_commands('section_report')
    if (not res):
        messagebox.showwarning("Error", c.error)
    else:    
        name = c.user.name 
        dirc = user_directory(name, c.c.name) #passing user name and console's class object's name attribute
        fname = os.path.basename(dirc)
        if (dirc != None):
            os.system('open ' + dirc + DIR_SEP + 'math_report.html' )
            os.system('open ' + dirc + DIR_SEP + 'reading_report.html' )
            os.system('open ' + dirc + DIR_SEP + 'writing_report.html' )

def get_new_class(): #function passes new class name from GUI button to console
    name = tkinter.simpledialog.askstring('New Class', 'Enter New Class Name')
    if(name != None):
        res = c.process_commands('new_class ' + name)
        if(not res and c.error is not None):  #if console's process_commands returns false and error msg exists
            messagebox.showwarning('Error', c.error)  #disply error on GUI
        else: 
            if(c.state == CLASS_STATE): #succesfully passed class object to console
                classname = c.c.name
                if(classname != None): # make sure objects name attribute is right
                    messagebox.showinfo('Current Class', 'Created Class ' + classname)
                    make_lc_button()  #update load class dropdown menu 
                    make_lu_button()

def get_load_class(cname):
    name = cname 
    if(name != None):
        res = c.process_commands('load_class ' + name)
        if(not res and c.error is not None):
            messagebox.showwarning("Error", c.error)
        else:
            if(c.state == CLASS_STATE): #make sure class object successfully passed to console
                if(c.c.name != None): #make sure loaded class objec has name attribute 
                    messagebox.showinfo('Current Class', 'Loaded Class ' + c.c.name)
                    make_lu_button()

def get_new_user():
    name = tkinter.simpledialog.askstring( 'New Student', 'Enter New Username')
    if(name != None):
        res = c.process_commands('new_student ' + name)
        if (not res):
            messagebox.showwarning("Error", c.error)
        else:     
            if(c.state == USER_STATE):
                if(c.user.name != None):
                     messagebox.showinfo('Current Student', 'Created Student ' + c.user.name)
                     users = list_users_array(c.c.name)
                     make_lu_button()
def get_load_user(uname):
    #name = tkinter.simpledialog.askstring( 'Load Student', 'Enter Username')
    name = uname
    if(name != None):
        res = c.process_commands('load_student ' + name)
        if (not res and c.error is not None):
            messagebox.showwarning("Error", c.error)
     
        else:    
          
            if(c.state == USER_STATE):
                if(c.user.name != None):
  
                    messagebox.showinfo('Current Student', 'Loaded Student ' + c.user.name)
                    users = list_users_array(c.c.name)
                    
def get_test_name():
   
     if(c.user is not None):
        file_path = tkinter.filedialog.askopenfilename( initialdir = './Users' + DIR_SEP + c.c.name + DIR_SEP + c.user.name )
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
                dirc = user_directory(name, c.c.name) 
                fname = os.path.basename(dirc)
                ans = messagebox.askyesno('Test Has Been Graded!', 'Would You Like To Open The Graded Test?')
                if (dirc != None and ans is True):
                    os.system('open ' + dirc + DIR_SEP + 'grade.html' )     
     else:
        messagebox.showwarning("Error", 'Please Load Or Create A Student First')           

def get_test_id(test_id):
    if(c.user is not None):
        name = test_id
        if(name != None):
            res = c.process_commands('answer_sheet ' + name)
            messagebox.showinfo('Answer Sheet', 'Created Answer Sheet ' + name)
            if (not res):
                messagebox.showwarning("Error", c.error)
    else:
        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 

def auto_gdr():
  foldername = tkinter.filedialog.askdirectory()
  if file_exists(foldername):
      list_of_tests = os.listdir(foldername)
      for filename in list_of_tests:
          if ".csv" in filename:
              pa = parse_answers(foldername + DIR_SEP + filename)
              name = pa.name
              if name == None or name not in list_users_array(c.c.name):
                  messagebox.showwarning("Error", 'Student name not found. ' + filename + ' was unable to be graded.') 
              else:
                  c.process_commands('load_student ' + name)
                  c.user.grade(pa)
                  c.process_commands('save')

def class_analyze(): #TODO: MOVE THIS TO class_analyze classname
  res = c.process_commands('class_analyze')
  if (not res):
      messagebox.showwarning("Error", c.error)


def college_profile():
    schoolname = []
    overall = []
    math = []
    reading = []
    writing = []
    school_overall = []
    schoolname = []
    school_m = []
    school_r = []
    school_w = []
    p_o = []
    p_m = []
    p_r = []
    p_w = []
    if(c.user is not None):

        if(len(c.user.tests_taken) is 0):

            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')
        else:
            for key, value in dict_overall.items():
                schoolname.append(key)
                school_overall.append(value)
            for key, value in dict_math.items():
                school_m.append(value)
            for key, value in dict_read.items():
                school_r.append(value)
            for key, value in dict_write.items():
                school_w.append(value)

            for test in c.user.tests_taken:
                overall.append(test.score_summary.total_score())
                math.append(test.score_summary.section_scores[MATH_TYPE])
                reading.append(test.score_summary.section_scores[READING_TYPE])
                writing.append(test.score_summary.section_scores[WRITING_TYPE])
                
            overalls = overall.pop()
            maths = math.pop()
            readings = reading.pop()
            writings = writing.pop()
            #print (overalls, maths, readings, writings)
            for school in schoolname:
                p_o.append((overalls/(dict_overall[school])))
                p_m.append((maths/(dict_math[school])))
                p_r.append((readings/(dict_read[school])))
                p_w.append((writings/(dict_write[school])))

            cp = College_Profile()
            dirc = user_directory(c.user.name, c.c.name)
            name = c.user.name

            cp.report(schoolname, p_o, p_m, p_r, p_w, name, c.c.name)
            
            os.system('open ' + dirc + DIR_SEP + 'college_profile.html')

    else:
    

        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 


def harvard():
    SCHOOLSCORE_O = dict_overall['Harvard']
    SCHOOLSCORE_M = dict_math['Harvard']
    SCHOOLSCORE_R = dict_read['Harvard']
    SCHOOLSCORE_W = dict_write['Harvard']
    SCHOOLNAME = 'Harvard'
    SCHOOLCOLOR = dict_colors['Harvard']
    SCHOOLBGCOLOR = dict_bgcolor['Harvard']
    messagebox.showinfo('School name', SCHOOLNAME)   
    if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
    else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 

def stanford():
   SCHOOLSCORE_O = dict_overall['Stanford']
   SCHOOLSCORE_M = dict_math['Stanford']
   SCHOOLSCORE_R = dict_read['Stanford']
   SCHOOLSCORE_W = dict_write['Stanford']
   SCHOOLNAME = 'Stanford'
   SCHOOLCOLOR = dict_colors['Stanford']
   SCHOOLBGCOLOR = dict_bgcolor['Stanford']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')   

def mit():
   SCHOOLSCORE_O = dict_overall['MIT']
   SCHOOLSCORE_M = dict_math['MIT']
   SCHOOLSCORE_R = dict_read['MIT']
   SCHOOLSCORE_W = dict_write['MIT']
   SCHOOLNAME = 'MIT'
   SCHOOLCOLOR = dict_colors['MIT']
   SCHOOLBGCOLOR = dict_bgcolor['MIT']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 
def yale():
   SCHOOLSCORE_O = dict_overall['Yale']
   SCHOOLSCORE_M = dict_math['Yale']
   SCHOOLSCORE_R = dict_read['Yale']
   SCHOOLSCORE_W = dict_write['Yale']
   SCHOOLNAME = 'Yale'
   SCHOOLCOLOR = dict_colors['Yale']
   SCHOOLBGCOLOR = dict_bgcolor['Yale']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')    
def uc_berkeley():
   SCHOOLSCORE_O = dict_overall['UC Berkeley']
   SCHOOLSCORE_M = dict_math['UC Berkeley']
   SCHOOLSCORE_R = dict_read['UC Berkeley']
   SCHOOLSCORE_W = dict_write['UC Berkeley']
   SCHOOLCOLOR = dict_colors['UC Berkeley']
   SCHOOLBGCOLOR = dict_bgcolor['UC Berkeley']
   SCHOOLNAME = 'UC Berkeley'
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')     
def ucla():
   SCHOOLSCORE_O = dict_overall['UCLA']
   SCHOOLSCORE_M = dict_math['UCLA']
   SCHOOLSCORE_R = dict_read['UCLA']
   SCHOOLSCORE_W = dict_write['UCLA']
   SCHOOLNAME = 'UCLA'
   SCHOOLCOLOR = dict_colors['UCLA']
   SCHOOLBGCOLOR = dict_bgcolor['UCLA']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 
def princeton():
   SCHOOLSCORE_O = dict_overall['Princeton']
   SCHOOLSCORE_M = dict_math['Princeton']
   SCHOOLSCORE_R = dict_read['Princeton']
   SCHOOLSCORE_W = dict_write['Princeton']
   SCHOOLNAME = 'Princeton'
   SCHOOLCOLOR = dict_colors['Princeton']
   SCHOOLBGCOLOR = dict_bgcolor['Princeton']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First') 
def caltech():
   SCHOOLSCORE_O = dict_overall['Caltech']
   SCHOOLSCORE_M = dict_math['Caltech']
   SCHOOLSCORE_R = dict_read['Caltech']
   SCHOOLSCORE_W = dict_write['Caltech']
   SCHOOLNAME = 'Caltech'
   SCHOOLCOLOR = dict_colors['Caltech']
   SCHOOLBGCOLOR = dict_bgcolor['Caltech']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')       
def johns_hopkins():
   SCHOOLSCORE_O = dict_overall['Johns Hopkins']
   SCHOOLSCORE_M = dict_math['Johns Hopkins']
   SCHOOLSCORE_R = dict_read['Johns Hopkins']
   SCHOOLSCORE_W = dict_write['Johns Hopkins']
   SCHOOLNAME = 'Johns Hopkins'
   SCHOOLCOLOR = dict_colors['Johns Hopkins']
   SCHOOLBGCOLOR = dict_bgcolor['Johns Hopkins']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')  
def carnegie_mellon():
   SCHOOLSCORE_O = dict_overall['Carnegie Mellon']
   SCHOOLSCORE_M = dict_math['Carnegie Mellon']
   SCHOOLSCORE_R = dict_read['Carnegie Mellon']
   SCHOOLSCORE_W = dict_write['Carnegie Mellon']
   SCHOOLNAME = 'Carnegie Mellon'
   SCHOOLCOLOR = dict_colors['Carnegie Mellon']
   SCHOOLBGCOLOR = dict_bgcolor['Carnegie Mellon']
   messagebox.showinfo('School name', SCHOOLNAME)
   if(c.user is not None):
        if(len(c.user.tests_taken) is 0):
            messagebox.showwarning("Error", 'Please take tests and grade them before generating reports.')

           
        else:
            c.user.c_graph_HTML(SCHOOLSCORE_O, SCHOOLSCORE_M, SCHOOLSCORE_R, SCHOOLSCORE_W, SCHOOLNAME, SCHOOLCOLOR, SCHOOLBGCOLOR)
            name = c.user.name 
            dirc = user_directory(name, c.c.name) 
            os.system('open ' + dirc + DIR_SEP + 'college_graph_report.html' )
   else:

        messagebox.showwarning("Error", 'Please Load Or Create A Student First')   

#Drop Down list Users 
def make_lu_button():
    LU = Menubutton(root, image =  LUimg, width = 254, height = 256)
    LU.grid(row = 1, column = 2, columnspan = 2, rowspan = 2,sticky = (W))
    LU.menu = Menu(LU)
    LU["menu"] = LU.menu
    if c.c == None:
      users = []
    else:
      users = list_users_array(c.c.name)
    for username in users:
        name = username
        LU.menu.add_radiobutton(label = name , command =lambda t = name: get_load_user(t))

#Drop Down Create Ans Sheet
def make_ans_sheet_button():
    CA = Menubutton(root, image = CASimg, width = 254, height = 256)
    CA.grid( row = 1, column = 4, columnspan = 2, rowspan = 2,sticky = (W))
    CA.menu = Menu(CA)
    CA["menu"] = CA.menu
    tests = list_tests()
    for test in tests:
        name = test
        CA.menu.add_radiobutton(label = name, command = lambda t = name: get_test_id(t))

def make_lc_button():
    LC = Menubutton(win, image =  LoadClass, width = 254, height = 256)
    LC.grid(row = 1, column = 2, columnspan = 2, rowspan = 2,sticky = (W))
    LC.menu = Menu(LC)
    LC["menu"] = LC.menu
    classes = list_classes()   #get list of classes in filesystem
    for Class in classes:  
        classname = Class
        LC.menu.add_radiobutton(label = classname , command =lambda t = classname: get_load_class(t)) #lambda to make function and pass params during runtime


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
##### SOME COMMANDS NOW HAVE PARAMS AND NEED TO BE UPDATED ****v v v v 

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

menu_help.add_command(label = 'Usage', command =  help_usage)
#display the menu
root.config(menu=menubar)
#######################################


# Logo
Label(root, image = photo, background = 'light steel blue').grid(row=0, column = 3, columnspan = 3) 


####### MAIN COLORED GUI BUTTONS 
if (c.state is CLASS_STATE or c.state is USER_STATE or c.state is LAUNCH_STATE): #if a class has been created or loaded, display class level user GUI
  

  Button( root, image = NUimg, width = 250, height = 250, pady = 0,  command= get_new_user).grid( row = 1, column = 0 ,columnspan = 2, rowspan = 2, sticky = (W))

  #Button( root, image = LUimg , width = 250, height = 250, pady = 0, command = get_load_user).grid(row = 1, column = 2, columnspan = 2, rowspan = 2,sticky = W)


  Button( root, image = Gimg, width = 250, height = 250,  pady = 0,  command = get_test_name ).grid( row = 1,column = 10, columnspan = 2, rowspan = 2,sticky = W)
   

  #Button( root, image = CASimg,  width = 250, height = 250, pady = 0 , command = get_test_id).grid( row = 1, column = 4, columnspan = 2, rowspan = 2,sticky = W)

  Button( root, image = Rstimg,  width = 250, height = 250, pady = 0, command = reset_user).grid( row = 9, column = 16, columnspan = 2, rowspan = 2,sticky = W)

  Button( root, image = Svimg,  width = 250, height = 250, pady = 0, command = save_user ).grid( row = 10, column = 2, columnspan = 2, rowspan = 2,sticky = W)

  Button( root, image = AutoGrdr,  width = 250, height = 250, pady = 0, command = auto_gdr ).grid( row = 10, column = 4, columnspan = 2, rowspan = 2,sticky = W)

  Button( root, image = ClassAnly, width = 250, height = 250, pady = 0, command = class_analyze ).grid( row = 9, column = 9, columnspan = 2, rowspan = 2, sticky =W)
  ## Reports Submenu Button

  mb = Menubutton( root, image = Rptimg, width = 254, height = 256)
  mb.grid(row = 10, column = 0, columnspan = 3, rowspan = 2, sticky = (W))
  mb.menu = Menu(mb)
  mb["menu"] = mb.menu
  mb.menu.add_checkbutton(label = "Simple Report", command = simple_report)
  mb.menu.add_checkbutton(label ="Advanced Report", command = advance_report)
  mb.menu.add_checkbutton(label ="Graphs Report", command = graph_report)
  mb.menu.add_checkbutton(label ="Section Report", command = section_report)


  # Goal School Drop down menu 
  Mb = Menubutton(root, image = GoalSchl, width = 254, height = 256)
  Mb.grid(row = 1, column = 16, columnspan = 3, rowspan = 2, sticky =(W))
  Mb.menu = Menu(Mb)
  Mb["menu"] = Mb.menu
  Mb.menu.add_radiobutton(label = "Harvard Report",  command = harvard) #textvariable = "Harvard", command = goal_school )
  Mb.menu.add_radiobutton(label = "Stanford Report", command = stanford )#command =)
  Mb.menu.add_radiobutton(label = "MIT Report", command = mit )#command =)
  Mb.menu.add_radiobutton(label = "Yale Report", command = yale)#command =)
  Mb.menu.add_radiobutton(label = "UC Berkeley Report", command = uc_berkeley)#command =)
  Mb.menu.add_radiobutton(label = "UCLA Report", command = ucla )#command =)
  Mb.menu.add_radiobutton(label = "Princeton Report", command = princeton ) #command =)
  Mb.menu.add_radiobutton(label = "Caltech Report", command = caltech)#command =)
  Mb.menu.add_radiobutton(label = "Johns Hopkins Report", command = johns_hopkins )#command =)
  Mb.menu.add_radiobutton(label = "Carnegie Mellon Report", command = carnegie_mellon)#command =)
  Mb.menu.add_radiobutton(label = "Complete College Profile", command = college_profile)
  
  
  make_ans_sheet_button()
  #if(c.c is not None):
  make_lu_button()
#else:  #if class has not been created or loaded yet display New/Load Class
  Button( win, image = NewClass, width = 250, height = 250, pady = 0,  command= get_new_class).grid( row = 1, column = 0 ,columnspan = 2, rowspan = 2, sticky = (W))



  make_lc_button() #make load class button 
# Tk enters its event loop
root.mainloop()


