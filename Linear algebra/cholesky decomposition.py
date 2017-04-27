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
# Problem - g -----------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-g-------------------------------------------------------------------"
"""A function to obtain cholesky decomposition of A, a symmetric and positive 
definite matrix. The function returns the lower variant triangular matrix,L."""

def CholeskyDecomp(A):          # function initialization
    n = A.shape[0]              # row dimension of A
    L = numpy.zeros((n,n))	# Create matrix L of zeros    
    for i in xrange(n):		# 3 for-loops initialization to perform cho-decomp
        for k in xrange(i+1):	
            s1 = sum(L[i,j] * L[k,j] for j in xrange(k))        # calculates sum
            if (i == k): 			                # Diagonal elements
                L[i,k] = sqrt(A[i,i] - s1)             # calculate diagonal elements of L
            else:
                L[i,k] = 1.0 / L[k,k] * (A[i,k] - s1)  # calculate off-diagonal elements
    print ('A_cholesky = \n%s' %L)                     # prints L
    return L                                           # returns L
    
#------------------------------------------------------------------------------------------------------------------
"""Testing CholeskeyDecomp function by using matrix 'A' from problem - a""" 

L = CholeskyDecomp(A)         # Apply our function
#print cholesky(A).T           # applying built-in function to compare results

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################

