import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

#####################################################################################################################
# Backtracking method------------------------------------------------------------------------------------------------
####################################################################################################################
print "--------------------BackTracking method---------------------------------"
#------------------------------------------------------------------------------------------------------------------
"""defining a function to perform Newton_raphson method, it takes function 'f'
it's derivatives 'df', initial value 'x0', error tolerance 'tol', and iteration number"""

def Backtracking(f,x0,h,step,e,nmax):
    n=1
    err = e*1.1
    while err > e and n < nmax:
        step = step - 0.1
        s = calcgradient(f,x0,h)
        xi = x0-step*s
        err = abs(f(xi) - f(x0))
        x0 = xi
        n = n+1
    return xi
#------------------------------------------------------------------------------------------------------------------    
"""test backtracking function"""

x0=np.array([8.0,9.0,9.0])
def f1(v): return np.sum((v-10)**2)+2
print Backtracking(f1,x0,0.1,1.0,0.0001,10)



