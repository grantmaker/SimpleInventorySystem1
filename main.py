# https://www.sourcecodester.com/tutorials/python/11417/python-simple-inventory-system.html
# Simple Inventory System in Python Tutorial

from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

# Setting up the Main Frame After importing the modules, we will now then create
# the main frame for the application.
# To do that just copy the code below and paste it inside the IDLE text editor

root = Tk()
root.title("Python: Simple Inventory System")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

# Designing the Layout After creating the Main Frame we will now add
# some layout to the application. Just kindly copy the code below and
# paste it inside the IDLE text editor.

# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Simple Inventory System", font=('arial', 45))
lbl_display.pack()

# Creating the Database Connection Then after setting up the design we will
# now create the database function. To do that just simply copy the code below
# and paste it inside the IDLE text editor.


