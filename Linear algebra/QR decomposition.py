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
# Problem - j-------------------------------------------------------------------------------------------------------
####################################################################################################################
#-------------------------------------------------------------------------------------------------------------------
print "-----------------------------Problem-j-------------------------------------------------------------------"
"""defining a function that normalizes a vector.It takes a vector 'x' as an input"""

def norm(x):
    return sqrt(sum([x_i**2 for x_i in x]))     # mathematical formula that used to normalize

#-------------------------------------------------------------------------------------------------------------------

""" defining a function named 'QRdecomp' to perform QR decomposition"""
"""this function takes an input 'A' as a matrix on which the QR decomposition will be applied"""

def QRdecomp(A):                                # initialization of the QRdecomp function
    n = A.shape[0]                              # dimension of columns of A matrix
    p = A.shape[1]                              # dimension of columns of A matrix
    Q = numpy.zeros((n,p))                      # a matrix of zeros,dim(A)=dim(Q), to store result
    V = numpy.matrix([[0.0]*p]*n)               # creating another matrix dim(A)=dim(V)of zeros
    V[:,[0]] = A[:,[0]]                         # initial orthogonal vector
    Q[:,[0]] = A[:,[0]]/norm(A[:,[0]])          # initial orthonormal vector from initial orthogonal vector    
 
    for j in range(1,p):                        # initializing a for loop 
        x = A[:,[j]]                            # second column of 'A' to get 2nd orthogonal vector
        v = numpy.matrix([[0.0]]*n)             # creating a vector of zeros to store result
        for k in range(1,j+1):                  # initializing another for loop nested in previous for loop
            vcl = V[:,[j-k]]                                        # most recent orthogonal vector
            s = numpy.multiply(float((x.T*vcl))/(vcl.T*vcl),vcl)    # multiplying a column of 'A' with orthogonal v. 
            v = v + s                                               # calculating to get next orthogonal vector
        V[:,[j]] = x - v                        # storing next orthogonal vector into V matrix
        Q[:,[j]] = V[:,[j]]/norm(V[:,[j]])      # storing orthonormal vector from last orthogonal vector
    R = Q.T*A
    print('Q = \n%s' % Q)                       # printing Q part of 'A'
    print('R = \n%s' % R)                       # printing R part of 'A'
    return (Q,R)    
    
#-------------------------------------------------------------------------------------------------------------------
"""Testing QRDecomp function by using matrix 'A' from problem - a"""

Q,R = QRdecomp(A)
#print numpy.around(Q*R,1)              # a matrix with rounded values
#print Q*R

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################
