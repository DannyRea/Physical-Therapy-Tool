import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import simpledialog
from tkinter import ttk
import matplotlib.lines as lines
from matplotlib.lines import Line2D

global newVal


def new_window(_class):  # Needed for new window (Patient / Phys)

    new = tk.Toplevel(main_screen)
    _class(new)


class logSuccess:
    def __init__(self, window):
        self.window = window

        Counter = 0
        size = 0.3
        yVal = 800

        # y = []
        # x = []

        # window = Toplevel(main_screen)



        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1200x700")  # Set overall size of screen

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Menu", menu=fileMenu)

        tabControl = ttk.Notebook(window)
        patientView = ttk.Frame(tabControl)
        analysisView = ttk.Frame(tabControl)
        tabControl.add(patientView, text='Patient View')
        tabControl.add(analysisView, text='Analysis View')
        tabControl.grid(sticky=NW)




        vals = np.array([[10., 10.], [80., 80.], [10., 10.]])  # Pie chart mod for # above Threshold
        vals2 = np.array([[20., 20.], [80., 80.], [20., 20.]])
        # val2=np.array([[20.,20.],[80.,80.],[20.,20.]])
        threshold = 1200

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)
        inner_colors = cmap([1, 2, 5, 6, 9, 10])

        # **********************************************************************
        def setFunc():

            plt.ion()

            threshold = simpledialog.askinteger("Theshold Value ", "Enter new value: ")  # FINALLY !!!

            a.plot([0., Counter], [threshold, threshold], "k--")
            print(threshold)

        # ******************************************************************
        def clear():
            # plt.ion()
            # threshold = 0
            newVal = simpledialog.askstring("Theshold Value ", "Enter new value: ")
            print(newVal)

        l1 = Label(patientView,
                   text="Data Selection",
                   font="bold")
        l2 = Label(patientView,
                   borderwidth=2,
                   width=20,
                   bg="mint cream",
                   relief="sunken",
                   text="Patient ID - Name")
        l3 = Label(patientView,
                   borderwidth=2,
                   width=20,
                   bg="mint cream",
                   relief="sunken",
                   text="Data Set - Primary")
        l4 = Label(patientView,
                   borderwidth=2,
                   width=20,
                   bg="mint cream",
                   relief="sunken",
                   text="Data Set - Secondary")

        R2 = Label(patientView,
                   text="Analysis Tools",
                   font="bold")
        checkbutton = Checkbutton(patientView, text="Autoscale")

        R3 = Label(patientView,
                   borderwidth=2,
                   width=20,
                   relief="sunken",
                   text="Data Set - Set New Thresholds")

        R4 = tk.Button(patientView,
                       borderwidth=2,
                       width=15,
                       text="Clear",
                       bg="mint cream",
                       command=clear)

        setThreshold = tk.Button(patientView,
                                 text="Set Threshold",
                                 bg="mint cream",
                                 command=setFunc)

        l1.grid(row=1, column=0, pady=10)
        l2.grid(row=2, column=0, pady=10)
        l3.grid(row=3, column=0, pady=10)
        l4.grid(row=4, column=0, pady=10)

        R2.grid(row=1, column=3, pady=10)
        # E1.grid(row = 3, column = 2, pady = 10)
        R4.grid(row=4, column=3, pady=20)

        checkbutton.grid(row=2, column=3, pady=10)
        setThreshold.grid(row=3, column=3, pady=10)

        y = []
        x = []

        with open('test.txt', 'r') as csvfile:  # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))
                x.append(Counter)
                if row:
                    Counter += 1

        fig = plt.figure(figsize=(6, 5), dpi=115)  # Sets Plot Graph Size
        # window.ax = fig.add_subplot(111, facecolor='#FFFFCC')
        # initial Threshold Set
        # plt.ion()
        a = fig.add_subplot(413)
        a.plot(x, y, label='Loaded from file!')
        a.plot([0., Counter], [threshold, threshold], "k--")
        a.set_xlabel('Time')
        a.set_ylabel('Force')

        b = fig.add_subplot(341)  # 441

        b.pie(vals.sum(axis=1), radius=1, colors=outer_colors,  # Outer plot
              wedgeprops=dict(width=size, edgecolor='w'))

        c = fig.add_subplot(344)  # 444

        c.pie(vals2.sum(axis=1), radius=1, colors=outer_colors,  # Outer plot
              wedgeprops=dict(width=size, edgecolor='w'))

        canvas = FigureCanvasTkAgg(fig, master=patientView)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2, rowspan=4, padx=50, pady=5)

        # navigation toolbar
        toolbarFrame = Frame(master=patientView)
        toolbarFrame.grid(row=4, column=3)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

        # window.cursor = Cursor(window.ax, useblit=True, color='red', linewidth=2)       #window. used for cursor

        # plt.tight_layout()
        # plt.show()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username  # Globals for patient database
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Login or Registor", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x300")
    Label(login_screen, text="Please enter login information").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


def register_user():  # registar Users into files in same DIR

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            # logSuccess()                                # Calls function with verification
            new_window(logSuccess)  # Class call for valid entry

        else:
            password_not_recognised()

    else:
        user_not_found()


def password_not_recognised():
    global password_not_recog_screen  # Failed login attempt

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# User not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    # menubar = Menu(main_screen)
    # main_screen.config(menu = menubar)

    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2",
           width="30",
           command=login).pack()

    Label(text="").pack()

    Button(text="Register",
           height="2", width="30",
           command=register).pack()

    main_screen.mainloop()


main_account_screen()
