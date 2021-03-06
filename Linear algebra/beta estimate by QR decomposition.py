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
# Problem - k -----------------------------------------------------------------------------------------------------
###################################################################################################################
print "-----------------------------Problem-k------------------------------------------------------------------"
"""A function to solve the system of eqn. AX=Y for X using QR decomposition"""
"""The function takes Q and R parts from QR decomp, and Y to return X as solution"""

def QRsolve(Q,R,Y):			# function initialization
    n = R.shape[0]                      # no. of rows in U matrix
    X = numpy.zeros((n))                # creates a vector of zeros
    b = Q.T*Y				# using Q to get suitable form of Y
    for i in range(n-1, -1, -1):        # two for loops initialization
        X[i] = b[i]                     # initial calculation for back substitution
        for j in range(i+1, n):
            X[i] = X[i] - R[i,j] * X[j] # 2-step calculation for back substitution
        X[i] = X[i] / R[i,i]            # final step calculation
    print('Beta_hat = \n%s' % X)		# print and return X
    return X
    
#-------------------------------------------------------------------------------------------------------------------
"""Testing QRsolve function by using matrix 'A' from problem - a"""

Q,R = QRdecomp(A)	# QRdecomp function to get QR decomposition
QRsolve(Q, R, Y)	# applying QRsolve function	 	

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################
