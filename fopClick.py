import csv
import os
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog, ttk
import mysql
from sshtunnel import SSHTunnelForwarder
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.widgets import Cursor
import mysql.connector as db
from HexToDec import HexToDec

global newVal
global line_1
global line_2


sacUser = input('SacLink username: ')
sacPass = input('SacLink password: ')

server = SSHTunnelForwarder(
    ("ecs-pw-proj-web.ecs.csus.edu", 22),
    ssh_host_key=None,
    ssh_username= sacUser,  # username goes here!
    ssh_password=sacPass,  # password goes here!
    remote_bind_address=("10.115.234.32", 3306))

server.start()

global cnx

cnx = mysql.connector.connect(user='bruteforce_user',
                              password='bruteforce_db',
                              host="127.0.0.1",
                              port=server.local_bind_port,
                              database='team_bruteforce')

if cnx is not None:
    print("Server connected")

db_cursor = cnx.cursor(buffered=True)

db_cursor.execute("SELECT * FROM TEST")
db_cursor.execute("SELECT * FROM TEST")
result = db_cursor.fetchall()

for row in result:
    print(row)
    print("\n")


# Creates a new window for patient and physician views
def new_window(_class):
    new = tk.Toplevel(main_screen)
    _class(new)


# ---------- Start ---------- User Login --------------------
# Creates foundation for login display.
def main_account_screen():
    global main_screen
    main_screen = tk.Tk()
    # menubar = Menu(main_screen)
    # main_screen.config(menu = menubar)

    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="#42e9f5", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2",
           width="30",
           command=login).pack()  # calls function login

    Label(text="").pack()

    Button(text="Register",
           height="2", width="30",
           command=register).pack()  # calls function register
    """
    Button(text="Exit Application",
           command=exit(0)).pack()  # Button to exit app
    """
    main_screen.mainloop()


# After initializing login display it asks for the user's info.
# From there appropriate methods are called for success or failure to login respectively.
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
    Button(login_screen, text="Login", width=10, height=1,
           command=login_verify).pack()  # calls login_verify to parse user file

    """
    Button(login_screen,
           text="Exit Application",
           command=sys.exit(0)).pack()  # Button to exit app
    """

# Verifies user login credentials against current list.
def login_verify():
    global username1

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:  # if username is found
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:  # if password is found
            # logSuccess()                               # Calls function with verification
            # new_window(logSuccess)                     # Class call for valid entry
            importFile()  # Call importFile for option for file destination

        else:
            password_not_recognised()  # calls password_not_recognised

    else:
        user_not_found()  # calls user_not_found


# Login Success.
# Maintains most functionality to see user appropriate data.
class logSuccess:
    def __init__(self, window):

        self.window = window

        global patientFname
        global patientLname
        

        highThreshold = 0
        lowThreshold = 0
        impactThreshold = 0
        highthreshCounter = 0
        lowthreshCounter = 0
        impactCounter = 0
        threshTot = 0
        seconds = 0
        totalCount = 0
        Counter = 0

        size = 0.3
        yVal = 800

        patientFname = "John"
        patientLname = "Doe"

        # window = Toplevel(main_screen)

        delete_importFile()  # Clean up import screen
        # delete_login()              # Clean up login screen

        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1700x1500")  # Set overall size of screen

        fileMenu = Menu(menubar)  # Sets drop down menu just exit is implemented right now
        fileMenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Menu", menu=fileMenu)

        tabControl = ttk.Notebook(window)

        splitView = ttk.Frame(tabControl)
        patientView = ttk.Frame(tabControl)
        analysisView = ttk.Frame(tabControl)

        tabControl.add(splitView, text='Split View')
        tabControl.add(patientView, text='Patient View')
        tabControl.add(analysisView, text='Analysis View')
        tabControl.grid(sticky=NW)

        # val2=np.array([[20.,20.],[80.,80.],[20.,20.]])
        # threshold = 1200

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)  # Random color generated for pie charts
        inner_colors = cmap([1, 2, 5, 6, 9, 10])  # Not being used but could at more depth for more data

        y = []  # x and y lists used to fill file data
        x = []
        plt_list = []

        with open(filename, 'r') as csvfile:  # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))  # Using data points as y-axis points
                x.append(Counter)
                if row:
                    Counter += 1  # Counting rows in text file and using them for x-axis

        for i in y:  # Number of impacts under set threshold
            if i < lowThreshold:
                lowthreshCounter+= 1
                continue

        for i in y:  # Number of impacts over set threshold
            if i > highThreshold:
                highthreshCounter+= 1
                continue


        for i in y:  # Number of impacts over ZERO
            if i > impactThreshold:
                impactCounter += 1
                continue

        for i in x:  # Number of impacts
            totalCount += 1

        second = totalCount / 250

        highthreshCalc = highthreshCounter / Counter  # % Calc
        lowthreshCalc = lowthreshCounter / Counter # % Calc
        threshTot = lowthreshCounter+lowthreshCounter

        print("Total Above: ", highthreshCounter)  # Output to make sure everything is right
        print("Total Below: ", lowthreshCounter)  # Output to make sure everything is right
        print("Total Impacts: ", impactCounter)
        print("Total Points: ", Counter)
        print("High Threshold %: ", highthreshCalc)
        print("Low Threshold %: ", lowthreshCalc)
        print("Total Thresh %: ", threshTot)
        print("Impact Counter: ", impactCounter)
        print("Total Count: ", totalCount)
        print("Seconds total: ", second)

        vals = np.array([[10., 10.], [highthreshCounter, highthreshCounter]])  # Setting pie chart %
        vals3 = np.array([[10., 10.], [lowthreshCounter, lowthreshCounter]])  # Setting pie chart %
        vals2 = np.array([[50., 50.], [10., 10.]])  #

        sizesB = [highthreshCalc, lowthreshCalc, (impactCounter - threshTot)]  # Setting pie b (Threshold) chart labels
        labelsB = '% Above', '% Below', 'Total %'

        sizesC = [7, 93]  # Setting pie c (Impact) chart labels
        labelsC = 'Above %', 'Total %'


        def setFunc():

            global line_1
            global line_2
            global line_3
            global line_4

            Counter = 0  # Set vals back to Zero
            highthreshCounter = 0
            lowthreshCounter = 0
            impactCounter = 0
            totalCount = 0

            y = []


            highThreshold = simpledialog.askinteger("Upper Threshold Value ", "Enter new value: ")  # FINALLY !!!
            lowThreshold = simpledialog.askinteger("Lower Threshold Value ", "Enter new value: ")  # FINALLY !!!

            print("In replot....")

            with open(filename, 'r') as csvfile:  # Re-set file designation
                plots = csv.reader(csvfile)
                for row in plots:
                    y.append(int(row[0]))  # Using data points as y-axis points
                    x.append(Counter)
                    if row:
                        Counter += 1  # Counting rows in text file and using them for x-axis

            for i in y:  # Number of impacts under set threshold
                if i < lowThreshold:
                    lowthreshCounter += 1
                    continue

            for i in y:  # Number of impacts over set threshold
                if i > highThreshold:
                    highthreshCounter += 1
                    continue

            for i in y:  # Number of impacts over ZERO
                if i > impactThreshold:
                    impactCounter += 1
                    continue

            for i in x:  # Number of impacts
                totalCount += 1
                continue

            highthreshCalc = highthreshCounter / Counter  # % Calc
            lowthreshCalc = lowthreshCounter / Counter  # % Calc
            threshTot = highthreshCounter + lowthreshCounter
            #threshTot = 1 - highthreshCalc

            print("In setFunc.......")  # Now IN Function
            print("Total Above: ", highthreshCounter)  # Output to make sure everything is right
            print("Total Below: ", lowthreshCounter)  # Output to make sure everything is right
            print("Total Impacts: ", impactCounter)
            print("Total Points: ", Counter)
            print("High Threshold %: ", highthreshCalc)
            print("Low Threshold %: ", lowthreshCalc)
            print("Total Thresh #: ", threshTot)
            print("Impact Counter: ", impactCounter)
            print("Total Count: ", totalCount)
            print("Seconds total: ", second)
            print(highThreshold)

            vals = np.array([[10., 10.], [highthreshCounter, highthreshCounter]])  # Setting pie chart %
            vals3 = np.array([[100., 100.], [lowthreshCounter, lowthreshCounter]])  # Setting pie chart %
            vals2 = np.array([[50., 50.], [10., 10.], [100., 100.]])  #

            sizesB = [highthreshCalc, lowthreshCalc, (impactCounter - threshTot)]  # Setting pie b (Threshold) chart labels
            #sizesB = [highthreshCalc, threshTot]  # Setting pie b (Threshold) chart labels
            labelsB = '% Above', '% Below', 'Total %'

            sizesC = [7, 93]  # Setting pie c (Impact) chart labels
            labelsC = 'Above %', 'Total %'

            # plt.ion()

            fig4 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value
            fig5 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value

            rePlot = fig4.add_subplot(1, 1, 1)  # Pie chart for client
            rePlot.set_title("Activity Peaks", fontsize=12)
            rePlot.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
                       # startangle sets starting point of % divisions
                       radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
                       wedgeprops=dict(width=size, edgecolor='w'),
                       textprops={'fontsize': 7})

            rePlotPV = fig5.add_subplot(1, 1, 1)  # Pie chart for client
            rePlotPV.set_title("Activity Peaks", fontsize=12)
            rePlotPV.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,
                         radius=1.2, shadow=True, startangle=180,  # colors are random right now calling outer_colors
                         wedgeprops=dict(width=size, edgecolor='w'),
                         textprops={'fontsize': 7})

            canvasRP = FigureCanvasTkAgg(fig4, master=splitView)
            # canvasRP.draw()
            canvasRP.get_tk_widget().grid(row=0, column=2, rowspan=4, padx=10,
                                          pady=150)  # Setting position of Pie chart threshold

            canvasPV = FigureCanvasTkAgg(fig5, master=patientView)
            # canvasPV.draw()
            canvasPV.get_tk_widget().grid(row=4, column=5, rowspan=4, padx=50,
                                          pady=150)  # Setting position of Pie chart threshold

            R3 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

            R4 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

            A6 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

            A7 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

            

            R3.grid(row=0, column=5, pady=2)
            R4.grid(row=1, column=5, pady=2)

            A6.grid(row=2, column=5, pady=2)
            A7.grid(row=3, column=5, pady=2)

            plt.ion()

            # threshold = simpledialog.askinteger("Theshold Value ", "Enter new value: ")  # FINALLY !!!
            if line_1:  # Checks to see if theres something in list, if so then pop it and remove line
                line = line_1.pop(0)
                line.remove()

            if not line_1:  # Checks empty list, and if true, plots the graph.
                line_1 = a.plot([0., Counter], [highThreshold, highThreshold], "k--")

            if line_2:  # For Analysis View
                line = line_2.pop(0)
                line.remove()

            if not line_2:
                line_2 = av.plot([0., Counter], [highThreshold, highThreshold], "k--")

            # threshold = simpledialog.askinteger("Threshold Value ", "Enter new value: ")  # FINALLY !!!
            if line_3:  # Checks to see if theres something in list, if so then pop it and remove line
                line = line_3.pop(0)
                line.remove()

            if not line_3:  # Checks empty list, and if true, plots the graph.
                line_3 = a.plot([0., Counter], [lowThreshold, lowThreshold], "k--")

            if line_4:  # For Analysis View
                line = line_4.pop(0)
                line.remove()

            if not line_4:
                line_4 = av.plot([0., Counter], [lowThreshold, lowThreshold], "k--")

            plt.ioff()  # Trapping updated threshold inbetween ion() & ioff() so only threshold get drawn

        def setThreshLine():
            global line_1
            global line_2
            global line_3
            global line_4

            line_1 = a.plot([0., Counter], [highThreshold, highThreshold], "k--")  # plots threshold line, assigns to list
            line_2 = av.plot([0., Counter], [highThreshold, highThreshold], "k--")  # plots threshold line, to Analysis View
            line_3 = a.plot([0., Counter], [lowThreshold, lowThreshold], "k--")  # plots threshold line, assigns to list
            line_4 = av.plot([0., Counter], [lowThreshold, lowThreshold], "k--")  # plots threshold line, to Analysis View

        def onpick(event):
            thisline = event.artist
            xdata = thisline.get_xdata()
            ydata = thisline.get_ydata()
            ind = event.ind
            points = tuple(zip(xdata[ind], ydata[ind]))
            #print('onpick points:', points)
            print(xdata[ind])
            print(ydata[ind])

            foP = ydata[ind]

            A15 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=foP)

            A15.grid(row=7, column=5, pady=2)


        #*********************************************************

        l1 = Label(splitView,
                   text="Above Threshold: ",
                   font="bold")

       # l6 = Label(splitView,
        #           text="Below Threshold: ",
        #           font="bold")

        l2 = Button(splitView,
                    text="Patient ID - Name: ",
                    font="bold",
                    command=patientSelection
                    )

        l3 = Label(splitView,
                   text="Data Set - Primary: ",
                   font="bold")

        l4 = Label(splitView,
                   text="Data Set - Secondary: ",
                   font="bold")

        l5 = Label(splitView,
                   text="Total Activity: ",
                   font="bold")

        R2 = Label(splitView,
                   text="Analysis Tools",
                   font="bold")

        l6 = Label(splitView,
                   text="Below Threshold: ",
                   font="bold")

        checkbutton = Checkbutton(patientView, text="Autoscale")  # Not being implemented but an example of setup

        R3 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

        R4 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

        R5 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=(patientFname + " " + patientLname))

        R6 = Label(splitView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=impactCounter)

        setThreshold = tk.Button(splitView,
                                 text="Set Thresholds",
                                 bg="mint cream",
                                 command=setFunc)  # command calls any function you want (setFunc, clear.....) !
        """
        replot = tk.Button(splitView,
                    text="Re-plot Graph",
                    bg="mint cream",
                    command=replotPIE)
        
        """

        # ******* Analysis View ************************************

        jerkCalc = 0
        rofD = 0
        foP = 0

        A1 = Label(analysisView,
                   text="Above Threshold: ",
                   font="bold")

        #A16 = Label(analysisView,
        #           text="Below Threshold: ",
        #           font="bold")


        A2 = Button(analysisView,
                    text="Patient ID - Name: ",
                    font="bold",
                    command=patientSelection
                    )

        A3 = Label(analysisView,
                   text="Data Set - Primary: ",
                   font="bold")

        A4 = Label(analysisView,
                   text="Data Set - Secondary: ",
                   font="bold")

        A5 = Label(analysisView,
                   text="Below Threshold: ",
                   font="bold")
        """
        R2 = Label(splitView,
                   text="Analysis Tools",
                   font="bold")

        checkbutton = Checkbutton(patientView, text="Autoscale")  # Not being implemented but an example of setup

        """

        A6 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=highthreshCounter)  # One way to display a calculated value

        A7 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=lowthreshCounter)

        A8 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=(patientFname + " " + patientLname))

        A9 = Label(analysisView,
                   borderwidth=10,
                   width=15,
                   relief="flat",
                   bg="mint cream",
                   text=impactCounter)

        setThresholdAV = tk.Button(analysisView,
                                   text="Set Thresholds",
                                   bg="mint cream",
                                   command=setFunc)  # command calls any function you want (setFunc, clear.....) !

        A10 = Label(analysisView,
                    text="Jerk: ",
                    font="bold")

        A11 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=jerkCalc)

        A12 = Label(analysisView,
                    text="Rate of Force: ",
                    font="bold")

        A13 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=rofD)

        A14 = Label(analysisView,
                    text="Force at point: ",
                    font="bold")

        A15 = Label(analysisView,
                    borderwidth=10,
                    width=15,
                    relief="flat",
                    bg="mint cream",
                    text=foP)
        """
        A16 = Label(analysisView,
                    text="Patient Notes",
                    font="bold")             #creates the header for Patient notes

        A17 = Text(analysisView,
                   height=20,
                   width=40)                 #creates the text box for patient notes

        """

        A1.grid(row=2, column=4, pady=2)
        A2.grid(row=2, column=0, pady=2)
        A3.grid(row=3, column=0, pady=2)
        A4.grid(row=4, column=0, pady=2)
        A5.grid(row=3, column=4, pady=2)
        A6.grid(row=2, column=5, pady=2)
        A7.grid(row=3, column=5, pady=2)
        A8.grid(row=2, column=1, pady=2)
        A9.grid(row=3, column=5, pady=2)
        A10.grid(row=5, column=4, pady=2)
        A11.grid(row=5, column=5, pady=2)
        A12.grid(row=6, column=4, pady=2)
        A13.grid(row=6, column=5, pady=2)
        A14.grid(row=7, column=4, pady=2)
        A15.grid(row=7, column=5, pady=2)
        #A16.grid(row=6, column=0, pady=2)
        #A17.grid(row=7, column=0, pady=2)

        setThresholdAV.grid(row=1, column=4, pady=5)

        # ***********************************************************

        l1.grid(row=0, column=4, pady=2)
        l2.grid(row=2, column=0, pady=2)
        l3.grid(row=3, column=0, pady=2)
        l4.grid(row=4, column=0, pady=2)
        l5.grid(row=3, column=4, pady=2)
        l6.grid(row=1, column=4, pady=2)

        R3.grid(row=0, column=5, pady=2)
        R4.grid(row=1, column=5, pady=2)
        R5.grid(row=2, column=1, pady=2)
        R6.grid(row=3, column=5, pady=2)

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

        # checkbutton.grid(row = 2, column = 6, pady = 5)
        setThreshold.grid(row=4, column=5, pady=5)
        # replot.grid(row=1, column=5, pady=5)

        fig1 = plt.figure(figsize=(6, 6), dpi=95)  # Instances of individual figures for alignment
        figAV = plt.figure(figsize=(10, 6), dpi=95)  # Instances of individual figures for alignment
        fig2 = plt.figure(figsize=(4, 3), dpi=95)  # figsize sets overall size of each figure
        fig3 = plt.figure(figsize=(4, 3), dpi=95)  # dpi zooms out and in with a change of value

        # plt.ion()
        a = fig1.add_subplot(1, 1, 1)  # Analysis View Graph plot
        av = figAV.add_subplot(1, 1, 1)  # Analysis View Graph plot
        # a.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
        a.plot(x, y, label='Loaded from file!')
        av.plot(x, y, label='Loaded from file!')

        line, = av.plot(x, y,'o',picker=0.01)  # 5 points tolerance         # For Force @ a point click event

        # a.plot([0., Counter], [highThreshold, highThreshold], "k--")            # Plotting threshold designation
        setThreshLine()
        a.set_xlabel('Time(seconds)')  # Set X axis title
        a.set_ylabel('Force in Newtons')  # Set Y axis title

        av.set_xlabel('Time(seconds)')  # Set X axis title
        av.set_ylabel('Force in Newtons')  # Set Y axis title
        # a.set_xticks(['0','10','20','30','40','50','60','70','80'])
        a.set_xticklabels(['0', '10', '20', '30', '40', '50', '60', '70', '80'])
        a.set_yticks(
            [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])  # Just using this right now but will most likely change

        av.set_xticklabels(['0', '10', '20', '30', '40', '50', '60', '70', '80'])
        av.set_yticks(
            [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000])  # Just using this right now but will most likely change
        # a.xticks(x,values)

        # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie

        b = fig2.add_subplot(1, 1, 1)  # Pie chart for client
        b.set_title("Activity Peaks", fontsize=12)
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

        # End pie chart code block for verification.
        # Instances of figs included into a single Canvas

        canvas1 = FigureCanvasTkAgg(figAV, master=analysisView)
        analysisView.cursor = Cursor(av, useblit=True, color='red', linewidth=2)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1, column=3, rowspan=4, padx=10,
                                     pady=10)
        # Setting positions of Analysis graph

        figAV.canvas.mpl_connect('pick_event', onpick)


        canvas1b = FigureCanvasTkAgg(fig1, master=splitView)
        splitView.cursor = Cursor(a, useblit=True, color='red', linewidth=2)  # Used for Analysis graph cursor
        canvas1b.draw()
        canvas1b.get_tk_widget().grid(row=1, column=3, rowspan=4, padx=10,
                                      pady=150)

        canvas2 = FigureCanvasTkAgg(fig2, master=splitView)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=2, rowspan=4, padx=10,
                                     pady=150)  # Setting position of Pie chart threshold

        canvas2b = FigureCanvasTkAgg(fig3, master=patientView)
        canvas2b.draw()
        canvas2b.get_tk_widget().grid(row=4, column=1, rowspan=4, padx=50,
                                      pady=150)  # Setting position of Pie chart threshold

        canvas3 = FigureCanvasTkAgg(fig3, master=splitView)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3, column=2, rowspan=4, padx=10,
                                     pady=150)  # Setting posision of Pie chart Impacts

        canvas3b = FigureCanvasTkAgg(fig2, master=patientView)
        canvas3b.draw()
        canvas3b.get_tk_widget().grid(row=4, column=5, rowspan=4, padx=50,
                                      pady=150)  # Setting position of Pie chart Impacts

        # navigational toolbar setup & pos
        toolbarFrame = Frame(master=splitView)
        toolbarFrame.grid(row=4, column=3)
        toolbar = NavigationToolbar2Tk(canvas1b, toolbarFrame)

        toolbarFrame = Frame(master=analysisView)
        toolbarFrame.grid(row=5, column=3)
        toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)


# Used for Analysis graph cursor


# Failed login attempt.
# Clears user input and informs user of failed login.
def password_not_recognised():
    global password_not_recog_screen

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()  # Destroys screen


# User not found.
# Clears user input and informs user of failed login.
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# -------------------- User Login ---------- End ----------


# ---------- Start ---------- User Registration --------------------
# This method displays a registration screen for the user.
# registration for doctor.
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Doctor Register")
    register_screen.geometry("300x420")

    global username  # Globals for patient database
    global password
    global username_entry
    global password_entry

    global email
    global phonenumber
    global fname
    global lname
    global doctorID
    global website

    global email_entry
    global phonenumber_entry
    global fname_entry
    global lname_entry
    global doctorID_entry
    global website_entry

    email = StringVar()
    phonenumber = StringVar()
    fname = StringVar()
    lname = StringVar()
    doctorID = StringVar()
    website = StringVar()

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Login or Register", bg="#42e9f5").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    # email text and enter box
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()

    phonenumber_lable = Label(register_screen, text="Phone Number * ")
    phonenumber_lable.pack()
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()

    website_lable = Label(register_screen, text="website * ")
    website_lable.pack()
    website_entry = Entry(register_screen, textvariable=website)
    website_entry.pack()

    fname_lable = Label(register_screen, text="First name * ")
    fname_lable.pack()
    fname_entry = Entry(register_screen, textvariable=fname)
    fname_entry.pack()

    lname_lable = Label(register_screen, text="Last name * ")
    lname_lable.pack()
    lname_entry = Entry(register_screen, textvariable=lname)
    lname_entry.pack()

    doctorID_lable = Label(register_screen, text="DoctorID(if Doctor) * ")
    doctorID_lable.pack()
    doctorID_entry = Entry(register_screen, textvariable=doctorID)
    doctorID_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#42e9f5",
           command=register_Doctor).pack()  # calls register_Doctor

    Button(register_screen,
           text="Exit Application",
           command=sys.exit(0)).pack()  # Button to exit app

# This method collects the Doctor's info. Then it saves the user's info into a File.
def register_Doctor():
    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    phonenumber_info = phonenumber.get()
    fname_info = fname.get()
    lname_info = lname.get()
    doctorID_info = doctorID.get()
    website_info = website.get()

    sql = "insert into TEST (user, num) values (%s, %s)"
    val = ('hello', int(18))

    # sql = "insert into TEST (user, num) values (%(users)s, %(number)s)"
    # val = {
    #   'users': 'hello',
    #    'number': 18,
    #    }
    db_cursor.execute(sql, val)
    cnx.commit()

    ##sql = "INSERT INTO DOCTOR (docID, licNum, phone, website) VALUES (%s, %s, %s, %s)"

    ##val = (ID_info, doctorID_info, phonenumber_info, website_info)

    ##db_cursor.execute(sql, val)

    ##sql = "INSERT INTO USER (ID, userName, passWord, email, userType, first_Name, last_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    ##val = (ID_info, username_info, password_info, email_info, userType_info(TRUE), fname_info, lname_info)

    ##db_cursor.execute(sql, val)

    ##db_connection.commit()

    file = open(username_info, "w")  # creates file with a user name and password

    file.write("userID" + "\n")  # need to get a method to create unique user IDs

    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info + "\n")
    file.write(phonenumber_info + "\n")
    file.write(website_info + "\n")
    file.write(fname_info + "\n")
    file.write(lname_info + "\n")
    file.write(doctorID_info + "\n")
    file.write("TRUE")  # true here being for doctor type.
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    phonenumber_entry.delete(0, END)
    website_entry.delete(0, END)
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    doctorID_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    # ----------------------------------------------separator between doctors registration and patient registration------------------


def registerPatient():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Patient Register")
    register_screen.geometry("300x420")

    global patient_username  # Globals for patient database
    global patient_password
    global patient_username_entry
    global patient_password_entry

    global patient_email
    global patient_fname
    global patient_lname

    global patient_email_entry
    global patient_fname_entry
    global patient_lname_entry

    patient_email = StringVar()
    patient_fname = StringVar()
    patient_lname = StringVar()

    patient_username = StringVar()
    patient_password = StringVar()

    Label(register_screen, text="Register a Patient", bg="#42e9f5").pack()
    Label(register_screen, text="").pack()

    patient_username_lable = Label(register_screen, text="Username * ")
    patient_username_lable.pack()
    patient_username_entry = Entry(register_screen, textvariable=username)
    patient_username_entry.pack()
    patient_password_lable = Label(register_screen, text="Password * ")
    patient_password_lable.pack()
    patient_password_entry = Entry(register_screen, textvariable=password, show='*')
    patient_password_entry.pack()

    # email text and enter box
    patient_email_lable = Label(register_screen, text="Email * ")
    patient_email_lable.pack()
    patient_email_entry = Entry(register_screen, textvariable=email)
    patient_email_entry.pack()

    patient_fname_lable = Label(register_screen, text="First name * ")
    patient_fname_lable.pack()
    patient_fname_entry = Entry(register_screen, textvariable=fname)
    patient_fname_entry.pack()

    patient_lname_lable = Label(register_screen, text="Last name * ")
    patient_lname_lable.pack()
    patient_lname_entry = Entry(register_screen, textvariable=lname)
    patient_lname_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#42e9f5",
           command=register_Patient).pack()  # calls register_Patient

    # This method collects the Patients's info. Then it saves the patient's info into a File.


def register_Patient():
    patient_username_info = username.get()
    patient_password_info = password.get()
    patient_email_info = email.get()
    patient_fname_info = fname.get()
    patient_lname_info = lname.get()

    ##sql = "INSERT INTO PATIENT (patID, bio, goals, lowThreshold, highThreshold) VALUES (%s, %s, %s, %s, %s)"

    ##val = (ID_info, bio_info(NULL), goals_info(NULL), lowThreshold_info(NULL), highThreshold_info(NULL))

    ##db_cursor.execute(sql, val)

    ##sql = "INSERT INTO USER (ID, userName, passWord, email, userType, first_Name, last_Name) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    ##val = (ID_info, username_info, password_info, email_info, userType_info(FALSE), fname_info, lname_info)

    ##db_cursor.execute(sql, val)

    ##db_connection.commit()

    file = open(patient_username_info, "w")  # creates file with a user name and password

    file.write("userID" + "\n")  # need to get a method to create unique user IDs

    file.write(patient_username_info + "\n")
    file.write(patient_password_info + "\n")
    file.write(patient_email_info + "\n")
    file.write(patient_fname_info + "\n")
    file.write(patient_lname_info + "\n")
    file.write("FALSE")  # false here being for being the patient type.
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# -------------------- User Registration ---------- End ----------


# -------------------- Patient Select ---------- Start ----------


def patientSelection():
    global patientSelect
    global patientFname
    global patientLname

    master = Tk()

    # create the label
    l1 = Label(master, text="Height")
    l2 = Label(master, text="Patient selection")

    # Grid
    l1.grid(row=0, column=0, sticky=W, pady=2)
    l2.grid(row=0, column=0, sticky=W, pady=2)

    patientFname = "Sarah"
    patientLname = "Doe"

    # sql stuff for fetching info from the DB

    # referenceLOGIN stuff - Should be elsewhere
    # mydb = mysql.connector.connect(
    # host="dbName??",
    #  user="userName",
    #   password="myPass"

    # )

    # DB select from Monitors table where login ID matches the Doc's ID
    # mycursor = mydb.cursor()

    # sql = "SELECT patientID FROM monitors WHERE docID = %s"
    # myVal = ("loginID")

    # mycursor.execute(sql, myVal)

    # myresult = mycursor.fetchall()

    # for x in myresult
    # myTable(x) = myresult(x)


# -------------------- Patient Select ------------- End ----------


# ---------- Start ---------- File Exploration  --------------------
# Allows user to browse through local files for data.
def browseFiles():
    global filename
    # delete_importFile()         # Clean up import screen

    filename = HexToDec(filedialog.askopenfilename(initialdir="/", title="Select a File", # Passes file to the
                                                   # HexToDec class. Returns filepath of modified file
                                                  filetypes=(("Text files", "*.txt*"),  # Only pulls txt files
                                                              ("all files", "*.*"))))

    fileExplorer.configure(text="File Opened: " + "" + filename)

    if os.stat(filename).st_size == 0:  # If file is not null open main class else no go!
        print('File is empty')

    else:
        print('File is not empty')

        new_window(logSuccess)  # Calls main class here!!!!!


# Allows user to search and import data from external service.
def importFile():
    global importFile_screen
    global fileExplorer

    delete_login()  # Clean up login screen
    importFile_screen = tk.Tk()

    importFile_screen.title('File Explorer')  # Window Title
    importFile_screen.geometry("350x300")
    importFile_screen.config(background="white")  # Set window background color
    fileExplorer = Label(importFile_screen,
                         text="File Explorer ",
                         width=50, height=4,
                         fg="blue")

    buttonExplore = Button(importFile_screen,
                           text="Browse Files",
                           command=browseFiles)  # Command call for browseFile function

    buttonExit = Button(importFile_screen,
                        text="Exit",
                        command=exit)  # Exits out of program

    fileExplorer.grid(column=0, row=1)  # Using grid layout
    buttonExplore.grid(column=0, row=2)
    buttonExit.grid(column=0, row=3)


# -------------------- File Exploration ---------- End ----------


# ---------- Start ---------- Remove Pop Ups From Display --------------------

def delete_login_success():
    login_success_screen.destroy()  # destroy instances of function when called


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def delete_importFile():
    importFile_screen.destroy()


def delete_login():
    login_screen.destroy()


# -------------------- Remove Pop Ups From Display ---------- End ----------

# This line starts the program by calling the beginning function.
main_account_screen()
