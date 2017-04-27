# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 4:  In this probelm we use "Naive Monte carlo(MC) method" to evaluate integral(a-c)
#----------------------------------------------------------------------------------------------------------------------------
#defining a function to perform the Niive MC mehtod.
# it takes 'a' and 'b', are lower and upper limit, 'infunc' is the integral, the number of values 'n' to be generated
# and 'fmax' that bounds the function.

def mc1int(a,b,n,infunc,fmax,s):                 # initializing the function
    random.seed(s)                               # initializing random number seeds
    N=0                                          # a variable to store to count the points
    for i in range(n):                           # initializing a for-loop
        x = random.uniform(a, b)                 # generating unif(a,b)
        y = random.uniform(0.0,fmax)             # generating unif(0,fmax)
        if y <= infunc(x):                       # initializing if condition, if satisfied then N will incease by 1 else 0
            N = N+1
        else:
            N = N+0
    random.seed()                                # stop the seeds
    A = (b-a)*fmax                               # calculating area
    I = A*N/n                                    # result of integral
    print(I)                                     # printing the final result

#---------------------------------------------------------------------------------------------------------------------------

s = 8675309                       # set seed

#(a) first integral to be computed
print 'Naive monte carlo method applied to integral a:'             # Printing what we do in this program
def infunc(x):                                                 
    I = (1/math.sqrt(2*math.pi))*math.exp(-float(x)**2/2)
    return (I)
# testing naive MC
mc1int(0.0,1.0,10000,infunc,20,s)

#---------------------------------------------------------------------------------------------------------------------------
#(b) second integral to be computed
print 'Naive monte carlo method applied to integral b:'             # Printing what we do in this program
def infunc(x):
    I = math.sin(2*x)**2/x**2
    return(I)

# testing naive MC
mc1int(math.pi,1.5*math.pi,10000,infunc,20,s)

#---------------------------------------------------------------------------------------------------------------------------
#(c) third integral to be computed
print 'Naive monte carlo method applied to integral c:'             # Printing what we do in this program
def infunc(x):
    I = x**(-float(1)/2)
    return(I)

# testing naive MC
mc1int(0.0,2.0,10000,infunc,20,s)


#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################




