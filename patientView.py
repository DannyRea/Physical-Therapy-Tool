import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import simpledialog, ttk
import matplotlib.lines as lines
from matplotlib.lines import Line2D
from tkinter import filedialog

global newVal
global line_1

# Just the patient view, nothing else

def new_window(_class):  # Needed to create new window (Patient / Phys) Views
    new = tk.Toplevel(main_screen)
    _class(new)

class patientView:
    def __init__(self, window):

        self.window = window

        Counter = 0
        threshold = 1100
        impactThreshold = 0
        threshCounter = 0
        impactCounter = 0
        threshTot = 0
        seconds = 0
        totalCount = 0
        root = Tk()

        size = 0.3

        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1500x1500")  # Set overall size of screen

        fileMenu = Menu(menubar)  # Sets drop down menu just exit is implemented right now
        fileMenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Menu", menu=fileMenu)

        tabControl = ttk.Notebook(window)
        patientView = ttk.Frame(tabControl)
        tabControl.add(patientView, text='Patient View')
        tabControl.grid(sticky=NW)

        # val2=np.array([[20.,20.],[80.,80.],[20.,20.]])
        threshold = 1200

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)  # Random color generated for pie charts
        inner_colors = cmap([1, 2, 5, 6, 9, 10])  # Not being used but could at more depth for more data

        y = []  # x and y lists used to fill file data
        x = []

        with open(filename, 'r') as csvfile:  # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))  # Using data points as y-axis points
                x.append(Counter)
                if row:
                    Counter += 1  # Counting rows in text file and using them for x-axis

        for i in y:  # Number of impacts over set threshold
            if i > threshold:
                threshCounter += 1
                continue

        for i in y:  # Number of impacts over ZERO
            if i > impactThreshold:
                impactCounter += 1
                continue

        for i in x:  # Number of impacts
            totalCount += 1
            continue

        threshCalc = threshCounter / Counter  # % Calc
        threshTot = 1 - threshCalc

        vals = np.array([[10., 10.], [threshCounter, threshCounter]])  # Setting pie chart %
        vals2 = np.array([[50., 50.], [10., 10.]])  #

        sizesB = [threshCalc, threshTot]  # Setting pie b (Threshold) chart labels
        labelsB = 'Above %', 'Total %'

        sizesC = [7, 93]  # Setting pie c (Impact) chart labels
        labelsC = 'Above %', 'Total %'

        p1 = Label(patientView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=("Impacts", impactCounter),
                   font="bold")

        p2 = Label(patientView,
                   text="Time period",
                   font="bold")

        p3 = Label(patientView,
                   text="Average Newtons",
                   font="bold")

        p4 = Label(patientView,
                   text="Total Datapoints",
                   font="bold")

        p1.grid(row=6, column=3)
        p2.grid(row=7, column=3)
        p3.grid(row=8, column=2)
        p4.grid(row=8, column=4)

        fig2 = plt.figure(figsize=(4, 3), dpi=95)  # figsize sets overall size of each figure
        fig3 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value

        b = fig2.add_subplot(1, 1, 1)  # Pie chart for client
        b.set_title("High Activity Peaks", fontsize=12)
        b.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
              # startangle sets starting point of % divisions
              radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
              wedgeprops=dict(width=size, edgecolor='w'),
              textprops={'fontsize': 7})

        c = fig3.add_subplot(1, 1, 1)
        c.set_title("Total Recorded Impacts", fontsize=12)
        c.pie(sizesC, labels=labelsC, autopct='%1.1f%%', colors=outer_colors,
              radius=1.2, shadow=True, startangle=180,
              wedgeprops=dict(width=size, edgecolor='w'),
              textprops={'fontsize': 7})

        canvas2 = FigureCanvasTkAgg(fig2, master=patientView)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=4, column=1, rowspan=4, padx=50,
                                     pady=150)  # Setting position of Pie chart threshold

        canvas3 = FigureCanvasTkAgg(fig3, master=patientView)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=4, column=5, rowspan=4, padx=50,
                                     pady=150)  # Setting position of Pie chart Impacts


def importFile():
    window = Tk()

    global fileExplorer

    window.title('File Explorer')  # Window Title
    window.geometry("500x500")
    window.config(background="white")  # Set window background color
    fileExplorer = Label(window,
                         text="File Explorer ",
                         width=100, height=4,
                         fg="blue")

    buttonExplore = Button(window,
                           text="Browse Files",
                           command=browseFiles)  # Command call for browseFile function

    buttonExit = Button(window,
                        text="Exit",
                        command=exit)  # Exits out of program

    fileExplorer.grid(column=1, row=1)  # Using grid layout
    buttonExplore.grid(column=1, row=2)
    buttonExit.grid(column=1, row=3)


def browseFiles():
    global filename

    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"),  # Only pulls txt files
                                                     ("all files", "*.*")))

    fileExplorer.configure(text="File Opened: " + filename)

    if os.stat(filename).st_size == 0:  # If file is not null open main class else no go!
        print('File is empty')

    else:
        print('File is not empty')
        new_window(patientView)  # Calls main class here!!!!!


def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    # menubar = Menu(main_screen)
    # main_screen.config(menu = menubar)

    main_screen.geometry("300x250")
    main_screen.title("Amputees")

    importFile()

    main_screen.mainloop()


main_account_screen()  # Calls main_account_screen()

