# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 5:  In this probelm we use "better Monte carlo(MC)" to evaluate integral(a-c)
# first define a function named "mc2int" for better MC.
# It takes 'a' and 'b' are lower and upper limits, 'n' is the number of points to be generated, 'infunc' is our
# desired function to be integrated, 'fmax' is not necessary here, and 's' is the random number seed

n = 10000                                       # number of points to be generated
s = 8675309                                     # a seed
fmax=0                                          # a value that bounds the function

def mc2int(a,b,n,infunc,fmax,s):                # initializing the better MC function
    random.seed(s)                              # initializing the random number's seed
    fmax = False
    fx = range(n)                               # initializing a variable to store integrated result
    for i in range(n):                          # initializing a for-loop
        x = random.uniform(a, b)                # genrating uniform(a,b)
        fx[i] = infunc(x)                       # using required integral and storing results in fx

    I = (b-a)*sum(fx)/n                         # Final result of our integration
    random.seed(s)                              # stopping random number's seed
    print(I)

#----------------------------------------------------------------------------------------------------------------------------
# definig the integral functions given in (a), (b), and (c).
# we will use this function according to the instruction given in the problems
#(a)
print 'Better monte carlo method applied to integral a:'             # Printing what we do in this program
def infunc(x):                                                 
    I = (1/math.sqrt(2*math.pi))*math.exp(-float(x)**2/2)
    return (I)

mc2int(0.0,1.0,n,infunc,fmax,s)                 # applyting MC function

#(b)------------------------------------------------------------------------------------------------------------------------
print 'Better monte carlo method applied to integral b:'             # Printing what we do in this program
def infunc(x):
    I = math.sin(2.0*x)**2/x**2
    return(I)
mc2int(math.pi,1.5*math.pi,n,infunc,fmax,s)     # applyting MC function

#(c)-------------------------------------------------------------------------------------------------------------------------
print 'Better monte carlo method applied to integral a:'             # Printing what we do in this program
def infunc(x):
    I = x**(-float(1.0)/2)
    return(I)

mc2int(0.0,2.0,n,infunc,fmax,s)                 # applyting MC function


#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################





