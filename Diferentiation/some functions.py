import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

###################################################################################################################
#--------------------------------------some differential options--------------------------------------------------
###################################################################################################################
#-------------------------------------------------------------------------------------------------------------------
print "-----------------------Any function-------------------------------------"
""" calculate a function using vector 
f(x) = x1^2 + x2^2 + ....... + xn^2 + 2"""

def f(v): return np.sum(v**2.0)+2.0
x=np.array([1.0,2.0,3.0])
print f(x)

#-------------------------------------------------------------------------------------------------------------------
print "----------------------calculate first derivative------------------------"
"""calculate 1st derivatives of 'f(x) = x^3 - 3'"""
def f(x): return x**3.0 - 3.0
def df(f,x0,h): return (f(x0+h) - f(x0-h))/(2.0*h)

# true value is 27, check several outputs.
#print df(f,3.0,1.0)
#print df(f,3.0,.5)
print df(f,3.0,10**(-6))

#-------------------------------------------------------------------------------------------------------------------
print "-----------------calculate 2nd derivative-------------------------------"
"""calculate 2nd derivatives of 'f(x) = x^3 - 3'"""
def df2(f,x0,h): return (f(x0+h) - 2.0*f(x0) + f(x0-h))/h**2.0
print df2(f,3.0,1.0)
