# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 7:  In this probelm we use extended midpoint rule to evaluate integral(a-c)
# In this problem we define a function named "midpoint", which takes two limits 'a' and 'b',
# a function 'infunc' given in the problem, maximum number of iterations 'nmax', and error tolerance 'e'

def midpoint(a,b,infunc,nmax,e):                          # initializing the function 
    n = 2                                                 # initila value of n is 2
    diff = 1.0                                            # initialiazing a variable to detect error 
    oldI = 0.0                                            # initializing another variable
    h = b-a                                               # initial heght of trapezoid
    I = (b-a)*infunc((a+b)/2.0)                           # 1st stage integration
    
    print 'iteration='+repr(1)+', Ivalue='+repr(I)+', error='+repr(1000)   # print 1st stage integration's output and error
    
    newI = I                                       # initializing a new variable to store integration in every iteration
    while diff >= e*abs(oldI) and n <= nmax:	   # starting while loop runs untill the given conditions are satisfied
            oldI = newI				   
            h = h/3.0
            newsum = 0.0                           # another new variable to store sum of the trapedoids' area
            for i in range(1, 2*3**(n-2)-1, 2):
                spot = 3.0*i*h/2                   # calculating new spot
                newsum = newsum + infunc(a+spot-h) + infunc(a+spot+h) # increment newsum by one step
            newI = oldI/3.0 + h*newsum
            diff = abs(newI - oldI)                                 # calculating error between two consequtive integration
            n = n + 1                                               # counting no. of iteration
            
            print 'iteration='+repr(n-1)+', Ivalue='+repr(newI)+', error='+repr(diff) # print all the desired outputs
    print(newI)                   # print the final result of the integration

#---------------------------------------------------------------------------------------------------------------------------
# definig a function given in (a) and we will use this function according to the instruction given in the problems
#(a): Extended midpoint rule for the integral(a)

print 'Extended Midpoint Rule applied to integral a:'             # Printing what we do in this program
def infunc(t):
    I = 1.0/(t*math.sqrt(2.0*math.pi))*math.exp(-(-math.log(t))**2/2.0)
    return(I)
#testing function
midpoint(0.0,1.0,infunc,12,10**(-6))

#(b)------------------------------------------------------------------------------------------------------------------------
print 'Extended Midpoint Rule applied to integral b:'             # Printing what we do in this program
def infunc(t):
    I = math.sin(2.0/t)**2
    return(I)
#testing function
midpoint(0.0,1.0/math.pi,infunc,12,10**(-6))

#(c)------------------------------------------------------------------------------------------------------------------------
print 'Extended Midpoint Rule applied to integral c:'             # Printing what we do in this program
def infunc(x):
    I = x**(-1.0/2.0)
    return(I)
#testing function
midpoint(0.0,2.0,infunc,12,10**(-6))


#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################





