# importing libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import math 
import csv
from scipy import stats

"""
(intercept) The intercept (often labeled as constant) is the point where 
the function crosses the y-axis. In some analysis, the regression 
model only becomes significant when we remove the intercept, and
the regression line reduces to Y = bX + error.

(rvalue) A correlation coefficient is a numerical measure of some type of 
correlation, meaning a statistical relationship between two variables. 
The variables may be two columns of a given data set of observations, 
often called a sample, or two components of a multivariate random 
variable with a known distribution

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
For paired data (x,y) we denote the standard deviation of the x data by sx and 
the standard deviation of the y data by sy.

The formula for the slope a of the regression line is:

r = rvalue

a = r(sy/sx)

https://en.wikipedia.org/wiki/Jerk_%28physics%29

Non-Linear change in slope

"""
x = []
y = []

x2 = []
y2 = []

x3 = []
y3 = []

s2 = 5000
f2 = 7000

s3 = 6300
f3 = 6400

Counter = 0

with open('test1.txt','r') as csvfile:                        # Set file designation
    plots = csv.reader(csvfile)
    for row1 in plots:
        y.append(int(row1[0]))
        x.append(Counter)
        if row1:
            Counter += 1

x2 = (x[s2:f2])			# List slicing!!
y2 = (y[s2:f2])

x3 = (x[s3:f3])
y3 = (y[s3:f3])

arrX = np.array(x3)		# Convert list into array for slope line CALC
arrY = np.array(y3)
 
# Initialise the subplot function using number of rows and columns 
figure, axis = plt.subplots(2, 2) 

res = stats.linregress(x3,y3)		# Calc performed on sub-array
print(res.slope)					# Average slope CALC

axis[0, 0].plot(x, y) 
axis[0, 0].set_title("Force vs. Time")

axis[0, 1].set_title("Sub-Array")
axis[0, 1].plot(x3, y3)

axis[1, 0].set_title("Line Regression Model")
axis[1, 0].plot(arrX, arrY, 'o', label='original data')
axis[1, 0].plot(arrX, res.intercept + res.slope*arrX, 'r', label='fitted line')

axis[1, 1].plot(x2, y2) 
axis[1, 1].set_title("Expanded View")

#plt.plot(arrX, arrY, 'o', label='original data')
#plt.plot(arrX, res.intercept + res.slope*arrX, 'r', label='fitted line')

plt.show() 