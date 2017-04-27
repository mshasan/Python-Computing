import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

#--------------------------------------------------------------------------------------------------------------------
print "---------------calculate gradient---------------------------------------"
"""calculate gradient, which is a vector of several derivatives
input: a function 'f', calculate gradient at 'x0', step difference 'h'
output: approximate gradient at x0"""
def f(v): return v[0]**2 + v[1]**2 + v[2]**2 + v[0]*v[1] - v[0]*v[2]

def calcgradient(f,x0,h):	
    n = x0.shape[0]			# calculate vector dimension
    grad = np.zeros(n)		# avector to store gradient
    for i in range(n):
        x1 = np.copy(x0)
        x2 = np.copy(x0)
        x1[i] = x0[i] - h		# two component of the derivatives
        x2[i] = x0[i] + h
        grad[i] = (f(x2) - f(x1))/(2.0*h)
    return grad

x0=np.array([1.5,6.0,13.5])
print calcgradient(f,x0,.005)