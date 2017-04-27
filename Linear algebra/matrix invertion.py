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
# problem - e ------------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-e-------------------------------------------------------------------"
print "---------------------------please see the last two matrices for the inverse--------------------------"
"""A function that invert a matrix, it takes 'A' matrix as input and gives
inverse of the A matrix"""

def InvertMatrix(A):                    # function initialization
    n = A.shape[0]                      # row dimension
    z = range(n)                        # initial permutation vector
    r = 0                               # initial swap tracking scalar
    A_decomp,z,r = LUdecomp(A,z,r)      # applying 'LUdecomp' function
    A_inv = [[0.0]*n]*n                 # a matrix of zeros to store inverse matrix
    Y = numpy.identity(n)               # an identity matrix need to get inverse
    for j in range(n):                          
        A_inv[j] = LUsolve(A_decomp,Y[j],z)             # using 'LUsolve' to get inverse
    print ('A_inverse = \n%s' % numpy.matrix(A_inv).T)  # prints inverse of A
    return A_inv

#-------------------------------------------------------------------------------------------------------------------
"""testing 'InvertMatrix' function, and comparing with numpy inverse matrix"""
"""need to stop 'print' options inside 'LUdecomp' and 'LUsolve' to get clean output"""

InvertMatrix(A)
print ('A_inverse from numpy = \n%s' % A.I)

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################

