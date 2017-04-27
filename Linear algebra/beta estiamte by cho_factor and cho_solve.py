#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################
"""some libraries to perform our desired calculations"""

import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import scipy                    # for decomposition and matrix
import numpy                    # for matrix operation
from scipy.linalg import *      # for linear algebra
from math import sqrt           # to perform square root 
from pprint import pprint       # to get better output interface

####################################################################################################################
#-------------------------------------------------------------------------------------------------------------------
"""Defining the given quadratic curve to simulate random data 
random.gauss(0.0,5.0)' generate Normal(0,25)'"""

def infunc(x):
    return(x*x + 3.0*x + 4.0 + random.gauss(0.0,5.0))

#-------------------------------------------------------------------------------------------------------------------
"""the function 'RandomData will be used ' to simulate random data, it takes 
n=# of simulation and s=random seed,"""

def RandomData(n,s):           
    random.seed(s)          # set seed
    one = range(n)          # a variable to store 1
    x = range(n)            # variable to store x
    x_sq = range(n)         # variable to store x square
    y = range(n)            # variable to store y
    for i in range(n):      # initializing a for loop to simulate data
        one[i] = 1                            # vector of one
        x[i] = random.uniform(-20.0, 20.0)    # vector of x
        x_sq[i] = x[i]**2                     # vector of x square
        y[i] = infunc(x[i])                   # vector of y
    random.seed(s)                            # stopping seed
    return (y,one,x,x_sq) # returns different variables required for design matrix
    
#-------------------------------------------------------------------------------------------------------------------
"""applying 'RandomData' function to simulate data"""
n = 100                         # number of simulated data
s = 897894321                   # random seed
y1,one,x,x_sq = RandomData(n,s)  

####################################################################################################################
# Problem - f------------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-f------------------------------------------------------------------"
"""uses of cho_factor and cho_solve to find 'beta_hat'"""
"""testing the functions by using matrix 'A' from problem - a. 

NOTE: we are using the same data we generated before but defining here again
to avoid overlapping of some variables' name"""

y2 = numpy.matrix([y1])                 # converting y vector into one dimensional matrix form
X = numpy.matrix([one,x,x_sq]).T        # design matrix
A = X.T*X                               # a matrix of X'X
Y = X.T*y2.T                            # vector of X'Y to form normal equation

c,lower = cho_factor(A)                 # using cho_factor function
print ('Beta_hat = %s' % cho_solve((c,lower),Y).T)     # getting beta_hat by using cho_solve function

#------------------------------------------------------------------------------------------------------------------
####################################################################################################################

