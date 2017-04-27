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
# Problem - m------------------------------------------------------------------------------------------------------
####################################################################################################################
print "-----------------------------Problem-m------------------------------------------------------------------"
"""A function to perform QR given rotation decomposition"""
"""it takes a matrix 'A' as input and gives R part of the QR decomposition"""

def GivensRotation(A):                  # function initialization
    n = A.shape[0]                      # row dimension of the matrix A
    p = A.shape[1]                      # column dimension of A
    Q = numpy.identity(n)               # initial Q matrix
    for j in range(p):                  # initializing a for loop
        I= numpy.identity(n)            # an identity matrix I
        for i in range(n-j-1):          # another for-loop
            B = numpy.copy(I)           # copy of I
            x1 = A[n-i-2,j]                     # first value to perform zero-out the lower element
            x2 = A[n-i-1,j]                     # 2nd value
            if x1 == 0.0: x1 = 0.000001         # if x1 and x2 are 0 then take these values to continue program
            if x2 == 0.0: x2 = 0.000001
            c = x1/(sqrt(x1**2 + x2**2))        # calculating c and k to get an orthogonal matrix
            k = x2/(sqrt(x1**2 + x2**2))
            CK = numpy.matrix([[c,k],[-k,c]])           # orthogonal matrix
            B[(n-i-2):(n-i),(n-i-2):(n-i)] = CK         # broadcasting orthogonal matrix into identity matrix
            Q = Q*numpy.matrix(B.T)                     # product of given rotation matrices
            A = B*A                                     # performing rotation by zero-out
    print('R = \n%s' % numpy.around(A,1))               # prints R matrix of rounded values
    return (Q,A) 
    
#-------------------------------------------------------------------------------------------------------------------
"""Testing GivensRotation function for QR decomposition by using 
    matrix 'A' from problem - a"""

Q,R = GivensRotation(A)
#print Q*R

#------------------------------------------------------------------------------------------------------------------
####################################################################################################################
