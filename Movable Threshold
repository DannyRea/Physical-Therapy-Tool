from tkinter import *       
import os

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.widgets import Cursor
import numpy as np
import csv



class pGraphOne:
    def __init__(self):
        
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, facecolor='#FFFFCC')
        self.c = ax.get_figure().canvas

        XorY = 2.0
        Counter = 0

        xGraph = []
        yGraph = []
        

        with open('test.txt','r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                yGraph.append(int(row[0]))
                xGraph.append(Counter)
                if row:
                    Counter += 1


        plt.plot(xGraph,yGraph, label='Loaded from file!')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Selected Data Set')
        plt.legend()

        xGraph = [-1, Counter]
        yGraph = [XorY, XorY]

        self.line = lines.Line2D(xGraph, yGraph, picker=5)
        ax.add_line(self.line)
        self.c.draw_idle()
        self.sid = self.c.mpl_connect('pick_event', self.clickonline)

        cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

        plt.show()


    def clickonline(self, event):
        if event.artist == self.line:
            print("line selected ", event.artist)
            self.follower = self.c.mpl_connect("motion_notify_event", self.followmouse)
            self.releaser = self.c.mpl_connect("button_press_event", self.releaseonclick)

    def followmouse(self, event):
        self.line.set_ydata([event.ydata, event.ydata])
        self.c.draw_idle()

    def releaseonclick(self, event):
        self.XorY = self.line.get_ydata()[0]

        print (self.XorY)

        self.c.mpl_disconnect(self.releaser)
        self.c.mpl_disconnect(self.follower)

#fig = plt.figure(figsize= (6,6))
#ax = fig.add_subplot(111, facecolor= '#FFFFCC')
Vline = pGraphOne()
#plt.show()
