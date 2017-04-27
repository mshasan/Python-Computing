# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 6:  n this probelm we use anithetic variable method to evaluate integral(a-c)
# definig a function named 'ANTint' to use anithetic condition. It takes 'a' and 'b', are lower and upper limits,
# 'n' is the number of points to be generated, 'infunc' is our desired function to be integrated, and 's' is the seed.

def ANTint(a,b,n,infunc,s):                  # intializing the function
    random.seed(s)                           # set seed
    x = range(n/2)                           # variables to store x's and y's values
    y = range(n/2)
    for i in range(n/2):                     # intializing a for-loop
        x[i] = random.uniform(a,b)           # generating unif(a,b) and storing in x
        y[i] = a+b-x[i]                      # generating y by using anithetic condition
    
    u = x+y                                  # merging two vectors
    fx = range(n)                            # a variable fx to store values after integration
    for i in range(n):                       # initializing another for-loop
        fx[i] = infunc(u[i])                 # performing integration

    I = (b-a)*sum(fx)/n                      # calcualting final integral's result
    random.seed(s)                           # stopping seeds
    print(I)                                 # printing final result

#----------------------------------------------------------------------------------------------------------------------------
# definig the integral functions given in (a), (b), and (c).
# we will use this function according to the instruction given in the problems
#(a)

s = 8675309                                                          # set seed
n = 10000                                                            # number of points to be generated

print 'Anthetic variable method applied to integral a:'             # Printing what we do in this program
def infunc(x):                                                 
    I = (1/math.sqrt(2*math.pi))*math.exp(-float(x)**2/2)
    return (I)

# testing function
ANTint(0.0,1.0,n,infunc,s)

#(b)------------------------------------------------------------------------------------------------------------------------
print 'Anthetic variable method applied to integral b:'             # Printing what we do in this program    
def infunc(x):
    I = math.sin(2*x)**2/x**2
    return(I)

# testing function
ANTint(math.pi,1.5*math.pi,n,infunc,s)

#(c)------------------------------------------------------------------------------------------------------------------------
print 'Anthetic variable method applied to integral c:'             # Printing what we do in this program
def infunc(x):
    I = x**(-float(1)/2)
    return(I)

# testing function
ANTint(0.0,2.0,n,infunc,s)


#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################


