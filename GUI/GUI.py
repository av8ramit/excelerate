#!/usr/bin/python

# import tkinter, load existing TK library on system
from tkinter import *
# import python's binding to newer "themed widgets" added to Tk in 8.5
from tkinter import ttk
#initiate main window
root = Tk()

#set window size
root.geometry("500x500")

#set window title
root.title("Excelerate")

# main frame that will hold all the widgets
mainframe = ttk.Frame(root, width = 500, height = 500, relief = SUNKEN)

#set up grid structure in main frame - sticky options for more precise widget placement
mainframe.grid(column = 0, row = 0, sticky =(N, W, E, S))

# row and column expansion if main window is resized
mainframe.rowconfigure(0, weight = 1)
mainframe.columnconfigure(0, weight = 1)

# Tk enters its event loop
root.mainloop()



