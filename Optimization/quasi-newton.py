import math                     # used to perform mathematical calculation
import random                   # used to generate random number
import numpy as np
import scipy                    # for decomposition and matrix
from math import exp,sin,cos,log,floor    # to use math modules
from scipy.optimize import * 

####################################################################################################################
#--------------------------some optimization options(more than one dimetional)-------------------------------------
####################################################################################################################


####################################################################################################################
# Quasi-Newton method------------------------------------------------------------------------------------------------
####################################################################################################################
#------------------------------------------------------------------------------------------------------------------
def f1(v): return np.sum((v-10)**2)+2        # a random function
x0=np.array([1.5,6.0,13.5])
#print calcgradient(f1,x0,.005)

#------------------------------------------------------------------------------------------------------------------
print "---------------Quasi-Newton method with DEF-----------------------------"
"""A function to perform Quasi-Newton method by using DFP-Davison-Fletcher-Powell formula
Input: f-function to be implemented, x0-initial vector,h-step size, 
step-constant step size for iteration, e-error tolerance,nmax-iteration number
Output: xi-minimized vector"""

def QuasiNewtonDFP(f,x0,h,step,e,nmax):      # function initialization
    n=1
    err = e*1.1
    p=x0.shape[0]                            # dimension of the initial vector
    H = np.identity(p)                       # an identitt matrix
    while err > e and n < nmax:                 
        I = np.identity(p)                   # another identity matrix
        s = np.dot(H,calcgradient(f,x0,h))   # get s by matrix multiplication H-hessian and gradient vector
        xi = x0 - step*s
        err = all(abs(calcgradient(f,xi,h) - calcgradient(f,x0,h))) # error calculation between two gradients vector
        x0 = xi
        y = calcgradient(f,(xi + s),h) - calcgradient(f,x0,h)   # calculate y
        gamma = 1/np.dot(y.T,s)
        A = gamma*np.dot(y.reshape(3,1),s.reshape(1,3))      # reshape vector to get suitable form
        H = np.dot(np.dot((I-A),H),(I-A)) + A             # new H-hessian matrix
        n = n+1
    return xi

#------------------------------------------------------------------------------------------------------------------
"""Test Quasis-newtonDFP function"""

def f1(v): return np.sum((v-10)**2)+2        # a random function
x0=np.array([8.0,9.0,9.0])                   # initial vector

print QuasiNewtonDFP(f1,x0,0.1,.01,.0001,100)      # applying the desired function

#------------------------------------------------------------------------------------------------------------------
print "---------------Quasi-Newton method with BFGS----------------------------"
"""A function to perform Quasi-Newton method by using Broyden-Fletcher-GS formula
Input: f-function to be implemented, x0-initial vector,h-step size, 
step-constant step size for iteration, e-error tolerance,nmax-iteration number
Output: xi-minimized vector"""

def QuasiNewtonBFGS(f,x0,h,step,e,nmax):     # function initialization
    n=1
    err = e*1.1
    p=x0.shape[0]                            # dimension of the initial vector
    H = np.identity(p)                       # an identitt matrix
    while err > e and n < nmax:                 
        I = np.identity(p)                   # another identity matrix
        s = np.dot(H,calcgradient(f,x0,h))   # get s by matrix multiplication H-hessian and gradient vector
        xi = x0 - step*s
        err = all(abs(calcgradient(f,xi,h) - calcgradient(f,x0,h))) # error calculation between two gradients vector
        x0 = xi
        y = calcgradient(f,(xi + s),h) - calcgradient(f,x0,h)        # calculate y
        U = np.dot(y.reshape(3,1),y.reshape(1,3))/np.dot(y,s)  # reshape vector to get suitable form
        V = -  np.dot(np.dot(H,np.dot(s.reshape(3,1),s.reshape(1,3))),H)/np.dot(np.dot(s,H),s)
        H = H + U + V             # new H-hessian matrix
        n = n+1
    return xi
    
#------------------------------------------------------------------------------------------------------------------
"""Test Quasis-newtonDFP function"""

def f1(v): return np.sum((v-10)**2)+2        # a random function
x0=np.array([8.0,9.0,9.0])                   # initial vector

print QuasiNewtonBFGS(f1,x0,0.1,.01,.0001,100)      # applying the desired function
