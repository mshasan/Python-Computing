import math                     # used to perform mathematical calculation
import random                   # used to generate random number
from math import exp,sin,cos,log,floor    # to use math modules

####################################################################################################################
# Naive quasi-newton method----------------------------------------------------------------------------------------
####################################################################################################################

"""defining a function to perform Newton_raphson method, it takes function 'f'
it's derivatives 'df', initial value 'x0', error tolerance 'tol', and iteration number"""

def NewtonRaphson(f,df,x0,tol,nmax):            # function initialization
    epsilon_a = 1.0                             # initial arbtrary error 
    n = 1                                       # intial iteration number
    while epsilon_a > tol and n < nmax:         # while-loop initialization
        xi = x0 - f(x0)/df(x0)
        epsilon_a = abs((xi - x0)/xi)           # calcualtion of the error
        error = epsilon_a*100                           
        n = n+1					# next iteration count
        x0 = xi
        m = floor(2.0- log(2.0*error,10))	# calculating significant digits at least corrected at the end 
    return xi
#------------------------------------------------------------------------------------------------------------------    
"""a function on which quasis newton will be applied"""

def f(x1,x2,x3): return 2*x1**2 + x2**2 + 3*x3**2
def df1(x1): return 4*x1
def df2(x2): return 2*x2
def df3(x3): return 6*x3
	
#------------------------------------------------------------------------------------------------------------------
"""a naive function to perform quasi-newton method"""

def NaiveQuasisNewton(f,df1,df2,df3,x1,x2,x3,a,tol,nmax):
    epsilon_a = 1.0                             # initial arbtrary error 
    n = 0                                       # intial iteration number
    def falpha(a): return 2.0*(x1 + df1(x1)*a)**2.0 + (x2 + df2(x2)*a)**2.0 + 3.0*(x3 + 6.0*a)**2.0
    def dfalpha(a): return 32.0*(x1 + df1(x1)*a) - 8.0*(x2 + df2(x2)*a) + 36.0*(x3 + 6.0*a)
    alpha = NewtonRaphson(falpha,dfalpha,a,10**(-4),10) # uses newton-raphson funcion to get alpha
    y = f(x1,x2,x3)
    print('n=%s,x1=%s,x2=%s,x3=%s,alpha=%s,f(x)=%s' % (n,x1,x2,x3,alpha,y))
    while epsilon_a > tol and n < nmax:
        x1 = x1 + df1(x1)*alpha
        x2 = x2 + df2(x2)*alpha
        x3 = x3 + df3(x3)*alpha
        def falpha(a): return 2.0*(x1 + df1(x1)*a)**2.0 + (x2 + df2(x2)*a)**2.0 + 3.0*(x3 + 6.0*a)**2.0
        def dfalpha(a): return 32.0*(x1 + df1(x1)*a) - 8.0*(x2 + df2(x2)*a) + 36.0*(x3 + 6.0*a)
        alpha = NewtonRaphson(falpha,dfalpha,a,10**(-4),10)
        y = f(x1,x2,x3)
	epsilon_a = abs((0.0 - x1)/x1)
	n = n+1
	print('n=%s,x1=%s,x2=%s,x3=%s,alpha=%s,f(x)=%s' % (n,x1,x2,x3,alpha,y))

#------------------------------------------------------------------------------------------------------------------
"""Test naive quasi newton method"""

NaiveQuasisNewton(f,df1,df2,df3,2.0,-2.0,1.0,0.915,10**(-4),10)

#-------------------------------------------------------------------------------------------------------------------
####################################################################################################################





