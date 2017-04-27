import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

####################################################################################################################
# Newton_raphson method -------------------------------------------------------------------------------------------
####################################################################################################################
print "--------------------------Newton_Raphson Method------------------------------------------------------------"
"""defineing the given function and its derivatives"""
def f(x): return x**3.0 - 0.165*x**2.0 + 3.993*10**(-4.0)	# given function
def df(x): return 3*x**2 - 0.33*x				# its derivatives
def f2(x): return x**3 - x - 1
def df2(x): return 3*x**2 - 1

####################################################################################################################
"""defining a function to perform Newton_raphson method, it takes function 'f'
it's derivatives 'df', initial value 'x0', error tolerance 'tol', and iteration number"""

def NewtonRaphson(f,df,x0,tol,nmax):            # function initialization
    epsilon_a = 1.0                             # initial arbtrary error 
    n = 1                                       # intial iteration number
    print('n=%s, x0=%s, error=%s, f(x)=%s' % (n,x0,"----",f(x0)))
    while epsilon_a > tol and n < nmax:         # while-loop initialization
        xi = x0 - f(x0)/df(x0)
        epsilon_a = abs((xi - x0)/xi)           # calcualtion of the error
        error = epsilon_a*100                           
        n = n+1					# next iteration count
        x0 = xi
        m = floor(2.0- log(2.0*error,10))	# calculating significant digits at least corrected at the end 
        print('n=%s, x0=%s, error=%s,m=%s, f(x)=%s' % (n,x0,error,m,f(xi)))
    print('Root = %s' % xi)
    return xi
    
#------------------------------------------------------------------------------------------------------------------    
"""test newton-raphson function"""

NewtonRaphson(f,df,0.05,10**(-4),10)		# applying newton raphson function
#NewtonRaphson(f2,df2,1.5,10**(-4),10)
#------------------------------------------------------------------------------------------------------------------
