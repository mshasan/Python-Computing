import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

####################################################################################################################
#------------------------------------some optimization options(one dimetional)-------------------------------------
####################################################################################################################

####################################################################################################################
# Bisection method------------------------------------------------------------------------------------------------
####################################################################################################################
print "-------------------------------Bisection Method------------------------------------------------------------"
"""the given function"""
def f(x): return x**3.0 - 0.165*x**2.0 + 3.993*10**(-4.0)
def f2(x): return x**2 - 3
def f3(x): return exp(-x)*(3.2*sin(x) - 0.5*cos(x))

#------------------------------------------------------------------------------------------------------------------
"""A function to perform bisection method, it takes a function 'f', lower value 
and upper value 'xl' and 'xu', error tolerance 'tol', and iteration number 'nmax'"""

def bisection(f,xl,xu,tol,nmax):                # function initialization
    epsilon_a = 1.0                             # initial arbtrary error 
    n = 1                                       # intial iteration
    xm = (xl + xu)/2.0                          # calculate midpoint
    print('n=%s, xl=%s, xu=%s, xm=%s, error=%s, f(x)=%s' % (n,xl,xu,xm,"----",f(xm)))
    func = f(xl)*f(xu)
    while epsilon_a > tol and n < nmax:         # while-loop initialization
        xm_old = xm
        if f(xl)*f(xm) < 0: xu = xm             # three condtions to proceed bisection
        elif f(xl)*f(xm) > 0: xl = xm 
        else: xm
        xm = (xl + xu)/2.0
        xm_new = xm
        epsilon_a = abs((xm_new - xm_old)/xm_new)       # calcualtion of error
        error = epsilon_a*100                           
        n = n+1
        m = floor(2.0- log(2.0*error,10))
        print('n=%s,xl=%s,xu=%s,xm=%s,error=%s,m=%s,f(x)=%s' % (n,xl,xu,xm,error,m,f(xm)))
    print('Root = %s' % xm)
    return xm
#------------------------------------------------------------------------------------------------------------------    
"""testing different function by using bisection method"""

bisection(f,0.0,0.11,10**(-4),10)                # applying bisection function
#bisection(f2,1.0,2.0,10**(-4),10)
#bisection(f3,3.0,4.0,10**(-4),10)



####################################################################################################################
# Bisection method------------------------------------------------------------------------------------------------
####################################################################################################################
print "-------------------------------Problem - 1: Bisection Method-------------------------------------------------"
"""the given function"""
def f1(x): return 50 - x**2 - x

#------------------------------------------------------------------------------------------------------------------
"""A function to perform bisection method 
Input: 
f: a function to be implemented
x0: lower limit 
x1: upper limit
tol: an error tolerance 
itmax: iteration number 
Output:
xm: the function's root""" 

def bisection(f,x0,x1,tol,itmax):               # function initialization
    epsilon_a = 1.0                             # initial arbtrary error 
    n = 1                                       # intial iteration
    xm = (x0 + x1)/2.0                          # calculate midpoint
    #print('n=%s, x0=%s, x1=%s, xm=%s, error=%s, f(x)=%s' % (n,x0,x1,xm,"----",f(xm)))
    func = f(x0)*f(x1)
    if func > 0:
        print "Error: The sign of the function doesn't change"
    while epsilon_a > tol and n < itmax:        # while-loop initialization
        xm_old = xm
        if f(x0)*f(xm) < 0: x1 = xm             # three condtions to proceed bisection
        elif f(x0)*f(xm) > 0: x0 = xm 
        else: xm
        xm = (x0 + x1)/2.0                      # calculate midpoint
        xm_new = xm
        epsilon_a = abs((xm_new - xm_old)/xm_new)       # calcualtion of the error
        error = epsilon_a*100                           
        n = n+1
        if n == itmax:
            print "Error: itmax is reached the limit"   # error message if iteration exced limit
        #print('n=%s, x0=%s, x1=%s, xm=%s, error=%s, f(x)=%s' % (n,x0,x1,xm,error,f(xm)))
    #print('Root = %s' % xm)
    return xm
    #m = floor(2.0- log(2.0*error,10))
    #print('Number of significant digit at least correct = %s' % m)
    
#------------------------------------------------------------------------------------------------------------------    
"""testing the bisection function """
print "Bisection method's, Root = "
print bisection(f1,0.0,100.0,10**(-6),100)  # applying bisection function

print "using scipy anderson function, Root = "
print anderson(f1,0)            # scipy built-in functionn to compare the result

"""Our function and SciPy function Anderson both gives almost the same root"""

#-------------------------------------------------------------------------------------------------------------------
###################################################################################################################
print "-------------------------------Problem - 2: Find All Roots-------------------------------------------------"
"""A function to be implemented"""
def f2(x): return sin(4*x)


"""A function to find out all roots"""
def FindAllRoots(f,x0,x1,n,tol,itmax):
    func = range(n)
    while any(func) < 0.0:
        points = np.linspace(x0,x1,n)               # creates equally spaced points
        func = range(n)
	for i in range(n):
            func[i] = f2(points[i-1])*f2(points[i]) # checking sign change
        
            n = 2*n
        print func
	
#    for j in range(len(func)):
#	if func[j] < 0.0:
#            roots[j] = bisection(f,points[j-1],points[j+1],tol,itmax) # root calculating 
#        else: roots = "None" 			
#	return roots
    
print FindAllRoots(f2,0.0,4.0*pi,4,10**(-6),10) # applying the function
