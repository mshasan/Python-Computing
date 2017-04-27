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


###################################################################################################################
# Problem - b -----------------------------------------------------------------------------------------------------
###################################################################################################################
print "-----------------------------Problem-b------------------------------------------------------------------"
"""Defining LU decomposition function, it takes a matrix 'A', a vector z, 
and r. The function returns decomposed 'A_new' matrix, permutation vector z,
even of odd swap tracking scalar r."""

def LUdecomp(A,z,r):
    n = A.shape[0]              # Generate initial index vector
    #z = range(n)                 
    
    s = [0] * n                 # a zero vector
    for i in xrange(n):         # two for loops to get largest element, used to get pivot
        smax = 0.0              # a initial value
        for j in xrange(n):                            
            smax = max(smax, abs(A[i,j]))       # finding maximum value in each row
        s[i] = smax                             # vector of largest values of each row

    for k in xrange(n-1):       # Begin Gaussian elimination.  
        rmax = 0.0              # initial value used to find the remaining row with the largest pivot.
        for i in xrange(k,n):
            r = abs(A[z[i],k]/s[z[i]])          # calculation to get right swap
            count = 0                           # a variable to count swap
            if r > rmax:
                rmax = r
                j = i
                count += 1                   # count increment by 1 if condition is satisfied
                
        r = 1 if (count%2.0 == 0.0) else -1  # checking even or odd         
        z[j],z[k] = (z[k],z[j])              # swap largest j-th pivotal row with the current row k

        for i in xrange(k + 1,n):            # next elimination carry out
            xmult = A[z[i],k]/A[z[k],k]      # required calculations
            A[z[i],k] = xmult
            for j in xrange( k + 1, n ):
                A[z[i],j] = A[z[i],j] - xmult*A[z[k],j] 
    print('A_decomp = \n%s, z = %s, and r = %s' % (A,z,r))	        # printing the results
    return (A,z,r)               # return decomposed matrix A, permutation vector z, and r

#------------------------------------------------------------------------------------------------------------------
"""testing the 'LUdecomp' function by using matrix 'A' from problem - a"""

n = A.shape[0]
z = range(n)
r = 0
A_decom,z,r = LUdecomp(A,z,r)                 # applying 'LUdecomp' function

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################

