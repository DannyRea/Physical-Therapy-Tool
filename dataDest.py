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
import matplotlib.lines as lines
from matplotlib.lines import Line2D
from tkinter import filedialog


global newVal


def new_window(_class):                                 # Needed to create new window (Patient / Phys) Views
        new = tk.Toplevel(main_screen)                          
        _class(new)


class logSuccess:
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

        size = 0.3  
        yVal = 800 
                                            
        #window = Toplevel(main_screen)
        
        menubar = Menu(window)
        window.config(menu=menubar)
        window.geometry("1500x1500")                                    # Set overall size of screen

        fileMenu = Menu(menubar)                                        # Sets drop down menu just exit is implemented right now
        fileMenu.add_command(label="Exit", command = window.quit)
        menubar.add_cascade(label="Menu", menu = fileMenu)


        #val2=np.array([[20.,20.],[80.,80.],[20.,20.]])
        threshold = 1200

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3)*4)                             # Random color generated for pie charts
        inner_colors = cmap([1, 2, 5, 6, 9, 10])                        # Not being used but could at more depth for more data

        y = []                                                      # x and y lists used to fill file data
        x = []
       
                
        with open(filename,'r') as csvfile:                         # Set file designation
            plots = csv.reader(csvfile)
            for row in plots:
                y.append(int(row[0]))                               # Using data points as y-axis points
                x.append(Counter)
                if row:                                             
                    Counter += 1                                    # Counting rows in text file and using them for x-axis

        for i in y:                                                 #  Number of impacts over set threshold
            if i > threshold:
                threshCounter += 1
                continue

        for i in y:                                                 #  Number of impacts over ZERO
            if i > impactThreshold:
                impactCounter += 1
                continue

        for i in x:                                                 #  Number of impacts 
            totalCount += 1
            continue

        
        second = totalCount / 250

          
        threshCalc = threshCounter / Counter                        # % Calc
        threshTot = 1 - threshCalc                                  
   
        print("Total Above: ", threshCounter)                       # Output to make sure everything is right
        print("Total Impacts: ", impactCounter)
        print("Total Points: ", Counter)
        print("Threshold %: ", threshCalc)
        print("Total Thresh %: ", threshTot)
        print("Impact Counter: ", impactCounter)
        print("Total Count: ", totalCount)
        print("Seconds total: ", second)
        

        vals = np.array([[10., 10.], [threshCounter,threshCounter]])                #  Setting pie chart %           
        vals2 = np.array([[50., 50.], [10.,10.]]) # 

        sizesB = [threshCalc, threshTot]                                            # Setting pie b (Threshold) chart labels
        labelsB = 'Above %', 'Total %'

        sizesC = [7, 93]                                                            # Setting pie c (Impact) chart labels
        labelsC = 'Above %', 'Total %'




    # **********************************************************************
        def setFunc():                                                                   # Not functioning correctly (still needs work!!!)

            plt.ion()

            threshold = simpledialog.askinteger("Theshold Value ", "Enter new value: ")    # FINALLY !!!

            a.plot([0., Counter], [threshold, threshold], "k--")
            print(threshold)



    # ******************************************************************
        def clear():                                                                    # Not being called as of now
            #plt.ion()
            #threshold = 0
            newVal = simpledialog.askstring("Theshold Value ", "Enter new value: ")
            print(newVal)


        # Grid widget designations 


        l1 = Label(window,
                text = "Threshold Exceeded: ",
                font = "bold")

        l2 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",                      # sets background color
                relief = "flat",                        # flat, grooved, raised, solid, sunken for different looks in gui
                text = "Patient ID - Name")
        l3 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",
                relief = "flat",
                text = "Data Set - Primary")
        l4 = Label(window, 
                borderwidth = 10,
                width = 20,
                bg = "mint cream",
                relief = "flat",
                text = "Data Set - Secondary")

        l5 = Label(window,
                text = "Total Activity: ",
                font = "bold")


        R2 = Label(window,
                text = "Analysis Tools",
                font = "bold")

        checkbutton=Checkbutton(window, text="Autoscale")           # Not being implemented but an example of setup
                                                                    
        R3 = Label(window, 
                borderwidth = 10,
                width = 20,
                relief = "flat",
                bg = "mint cream",
                text = threshCounter)               # One way to display a calculated value
        
        """
        R4 = tk.Button(window, 
                borderwidth = 2,
                width = 20,
                text = "Clear",
                bg = "mint cream",
                command = clear)
        """
                  
        R5 = Label(window, 
                borderwidth = 10,
                width = 20,
                relief = "flat",
                bg = "mint cream",
                text = impactCounter)

        setThreshold = tk.Button(window,
                text="Set Threshold",
                bg = "mint cream",
                command = setFunc)                  # command calls any function you want (setFunc, clear.....) !

        l1.grid(row = 2, column = 4, pady = 5)                 
        l2.grid(row = 2, column = 0, pady = 5)
        l3.grid(row = 3, column = 0, pady = 5)
        l4.grid(row = 4, column = 0, pady = 5)
        l5.grid(row = 3, column = 4, pady = 5)
        R3.grid(row = 2, column = 5, pady = 5)
        R5.grid(row = 3, column = 5, pady = 5)

        #checkbutton.grid(row = 2, column = 6, pady = 5)
        setThreshold.grid(row = 4, column = 5, pady = 5)
       
        fig1 = plt.figure(figsize=(6,6), dpi = 95)                      # Instances of individual figures for alignment
        fig2 = plt.figure(figsize=(4,3), dpi = 95)                      # figsize sets overall size of each figure 
        fig3 = plt.figure(figsize=(4,3), dpi = 95)                      # dpi zooms out and in with a change of value
    
        #plt.ion()
        a = fig1.add_subplot(1,1,1)                                     # Analysis View Graph plot
        #a.subplots_adjust(bottom=0.1, right=0.8, top=0.9)             
        a.plot(x,y, label='Loaded from file!')
        a.plot([0., Counter], [threshold, threshold], "k--")            # Plotting threshold designation     
        a.set_xlabel('Time(seconds)')                                   # Set X axis title
        a.set_ylabel('Force in Newtons')                                # Set Y axis title
        #a.set_xticks(['0','10','20','30','40','50','60','70','80'])
        a.set_xticklabels(['0','10','20','30','40','50','60','70','80'])    
        a.set_yticks([0,250,500,750,1000,1250,1500,1750,2000])          # Just using this right now but will most likely change
        #a.xticks(x,values)
 
        # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie

        b = fig2.add_subplot(1,1,1)                                             # Pie chart for client               
        b.set_title("High Activity Peaks", fontsize = 12)
        b.pie(sizesB, labels=labelsB, autopct='%1.1f%%', colors=outer_colors,   # startangle sets starting point of % divisions
                    radius=1.2, shadow=True, startangle=180,                    # colors are random right now calling outer_colors
                    wedgeprops=dict(width=size, edgecolor='w'),             
                    textprops={'fontsize': 7})
  
        c = fig3.add_subplot(1,1,1)          
        c.set_title("Total Recorded Impacts", fontsize = 12)
        c.pie(sizesC, labels=labelsC, autopct='%1.1f%%', colors=outer_colors,
                    radius=1.2, shadow=True, startangle=180,
                    wedgeprops=dict(width=size, edgecolor='w'),
                    textprops={'fontsize': 7})

                                                                                # End pie chart code block for verification.
        # Instances of figs included into a single Canvas
        
        canvas1 = FigureCanvasTkAgg(fig1, master=window)                        
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=1, column=3, rowspan = 4, padx = 10, pady = 150)  # Setting positions of Analysis graph    

        canvas2 = FigureCanvasTkAgg(fig2, master=window)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=2, rowspan = 4, padx = 10, pady = 150)   # Setting position of Pie chart threshold         

        canvas3 = FigureCanvasTkAgg(fig3, master=window)
        canvas3.draw()
        canvas3.get_tk_widget().grid(row=3, column=2, rowspan = 4, padx = 10, pady = 150)   # Setting posision of Pie chart Impacts     

                                                                                            # navigational toolbar setup & pos
        toolbarFrame = Frame(master=window)
        toolbarFrame.grid(row=4,column=3)
        toolbar = NavigationToolbar2Tk(canvas1, toolbarFrame)
        
        window.cursor = Cursor(a, useblit=True, color='red', linewidth=2)       #   Used for Analysis graph cursor



def register():

    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x400")
 
    global username                                         # Globals for patient database
    global password
    global username_entry
    global password_entry
    
    global email
    global phonenumber
    global fname
    global lname
    global doctorID
    
    global email_entry
    global phonenumber_entry
    global fname_entry
    global lname_entry
    global doctorID_entry
    
    email = StringVar()
    phonenumber = StringVar()
    fname = StringVar()
    lname = StringVar()
    doctorID = StringVar()
    
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
    
        #email text and enter box
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    
    phonenumber_lable = Label(register_screen, text="Phone Number * ")
    phonenumber_lable.pack()
    phonenumber_entry = Entry(register_screen, textvariable=phonenumber)
    phonenumber_entry.pack()
    
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
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()     # calls registar_user
 
 
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
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()       # calls login_verify to parse user file
 
 
def register_user():                                    # registar Users into files in same DIR

    username_info = username.get()
    password_info = password.get()
    email_info = email.get()
    phonenumber_info = phonenumber.get()
    fname_info = fname.get()
    lname_info = lname.get()
    doctorID_info = doctorID.get()
    
    ##sql = "INSERT INTO employee (username, password) VALUES (%s, %s)"

    ##val = (username_info, password_info)

    ##db_cursor.execute(sql, val)

    ##db_connection.commit()
 
    file = open(username_info, "w")         # creates file with a user name and pswd
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info + "\n")
    file.write(phonenumber_info + "\n")
    file.write(fname_info + "\n")
    file.write(lname_info + "\n")
    file.write(doctorID_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    phonenumber_entry.delete(0, END)
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    doctorID_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()



# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()           
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()                        
    if username1 in list_of_files:                      # if username is found
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:                         # if pswd is found
            #logSuccess()                               # Calls function with verification 
            #new_window(logSuccess)                     # Class call for valid entry
            importFile()                                # Call importFile for option for file destination
 
        else:
            password_not_recognised()                   # calls password_not_recognised
 
    else:
        user_not_found()                                # calls user_not_found
 


def importFile():
    window = Tk()

    global fileExplorer

    window.title('File Explorer')                               # Window Title
    window.geometry("500x500")                                      
    window.config(background = "white")                         # Set window background color
    fileExplorer = Label(window, 
                                text = "File Explorer ",
                                width = 100, height = 4, 
                                fg = "blue")     
          
    buttonExplore = Button(window, 
                            text = "Browse Files",
                            command = browseFiles)              # Command call for browseFile function
      
    buttonExit = Button(window, 
                         text = "Exit",
                         command = exit)                        # Exits out of program
    
    fileExplorer.grid(column = 1, row = 1)                      # Using grid layout   
    buttonExplore.grid(column = 1, row = 2)    
    buttonExit.grid(column = 1,row = 3)

def browseFiles():
    global filename
    
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
                                            filetypes = (("Text files", "*.txt*"),          # Only pulls txt files
                                                       ("all files", "*.*")))
      
    fileExplorer.configure(text="File Opened: "+filename)

    if os.stat(filename).st_size == 0:                      # If file is not null open main class else no go!
        print('File is empty')                                          
      
    else:
        print('File is not empty')
        new_window(logSuccess)                              # Calls main class here!!!!!
     
 
def password_not_recognised():                          
    global password_not_recog_screen                        # Failed login attempt

    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()     # Destroys screen
 
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
    login_success_screen.destroy()                      # destroy instances of function when called
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
             

def main_account_screen():                      # Parent Node
    global main_screen
    main_screen = tk.Tk()
    #menubar = Menu(main_screen)
    #main_screen.config(menu = menubar)

    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Login", height="2",
            width="30",
            command = login).pack()             # calls function login

    Label(text="").pack()

    Button(text="Register",
            height="2", width="30",
            command=register).pack()            # calls function register

    main_screen.mainloop()
 
 
 
main_account_screen()                   # Calls main_account_screen()
