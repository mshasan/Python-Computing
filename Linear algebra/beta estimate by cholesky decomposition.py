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
# Problem - h -----------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-h-----------------------------------------------------------------"
"""Defining 'CHOsolve' function, it takes a matrix 'B', two vectors Y and z"""
""" The function returns Y, which is the final solution of a equn. system."""
"""NOTE: My function's name is 'CHOsolve' instead of LUsub, because professor
confirmed me LUsub for LUdecomp is different from LUsub used for choloskey"""

def CHOsolve(L,b):                      # function initialization
    n = L.shape[0]                      # row dimension
    x = numpy.zeros(n)                  # a matrix of zeros
    for i in range(n):                  # starting forward subtitution
        x[i] = b[i]/L[i,i]              # initial value
        for j in range(0,i):            # 2nd for loop
            x[i] = x[i] - L[i,j]*x[j]   # calculation for forward substitution  
            x[i] = x[i]/L[i,i]          # final value after forward sus.

    for i in range(n-1,-1,-1):          # starting backward substitution
        x[i] = x[i]                     # initial value
        for j in range(i+1,n):
            x[i] = x[i] - L.T[i,j]*x[j] # required calculation inside of the back subs.    
        x[i] = x[i]/L.T[i,i]
    print ('Beta_hat = %s' % x)                # prints result
    return x                            # return solution

#------------------------------------------------------------------------------------------------------------------
"""Using CholeskeyDecomp and CHOsolve functions to get beta_hat"""

L = CholeskyDecomp(A)           # applying CholeskeyDecomp to get L matrix
CHOsolve(L,Y)                   # applying CHOsolve to get beta_hat

#------------------------------------------------------------------------------------------------------------------
####################################################################################################################


