import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

####################################################################################################################
# Conjugate gradient method------------------------------------------------------------------------------------------------
####################################################################################################################
#-------------------------------------------------------------------------------------------------------------------
print "----------------conjugate gradient method-------------------------------"
"""function to perform conjugate gradient
Input: f-function to be minimized,x0-starting point, h-step size in gradient,
e-error, step-constant step size for each iteration
ouput: xnew-coordinates of local minimum for f"""

def ConjugateGradient(f,x0,h,step,e,nmax):
    n=1
    err = e*1.1
    while err > e and n < nmax:
        s = calcgradient(f,x0,h)
        step = step - .1
        xi = x0 + step*s
        err = abs(f(xi) - f(x0))
        x0 = xi
        n = n+1
    return xi
#-------------------------------------------------------------------------------------------------------------------
"""a function to be implemented 
f(x,y,x) = (x-10)^2+(y-10)^2+(z-10)^2+2"""
def f1(v): return np.sum((v-10)**2)+2

x0=np.array([8.0,9.0,9.0])
print ConjugateGradient(f1,x0,0.1,.01,0.0001,20)


