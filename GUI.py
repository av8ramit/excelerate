from tkinter import *
from tkinter.messagebox import askyesno


#response = askyesno("Important Question", "Do you like CS 61A?")
def handle_button_push():
    print("Button pushed.")

root = Frame()
root.grid()
root.rowconfigure(0, pad=100)
root.columnconfigure(0, pad=200)
root.master.title("Excelerate")

button = Button(root, text="Start Button!", command=handle_button_push)

button1 = Button(root, text="Start Button!", command=handle_button_push)
button.grid(row=0, column=0)
button1.grid(row=5, column=5)
root.mainloop()