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
# Problem - c -----------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-c--------------------------------------------------------------------"
"""Defining LUsolve function, it takes a matrix 'B', two vectors Y and z"""
""" The function returns Y, which is the final solution of a equn. system."""
"""NOTE: My function's name is LUsolve instead of LUsub, because professor 
asked LUsolve later, and he also confirmed me it is a typo"""

def LUsolve(B,Y,z ):                      # function initialization
    n = B.shape[0]                        # no. of rows of matrix 
    U = triu(B)                           # U part from LU decomposition
    L = tril(B,k=-1) + numpy.identity(n)  # L part from LU decomposition
    
    x = numpy.zeros(n)                    # Starts Forward substitution
    for k in xrange(n-1):
        for i in xrange(k+1,n):
            Y[z[i]] = Y[z[i]]- L[z[i],k]*Y[z[k]]        # forward calculation

    for i in xrange(n-1,-1,-1):           # Starts Backward substitution
        sum = Y[z[i]]
        for j in xrange(i+1,n):           # starts 2nd for-loop
            sum = sum - U[z[i],j]*x[j]    # required calculation for backward sub.
        x[i] = sum / U[z[i],i]
    
    print ('L = \n%s' % L)
    print ('U = \n%s' % U) 
    print ('Beta_hat = %s' % x)                  # prints solution
    return x                              # return solution
    
#-------------------------------------------------------------------------------------------------------------------
""""testing the 'LUdecomp' function by using matrix 'A_decomp' and permutation
vector z from problem - b, and Y vector from problem - A"""

LUsolve(A,Y,z)          # applying LUsolve function

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################
