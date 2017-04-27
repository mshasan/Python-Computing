# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 8:  In this probelm we use "Importance sampling" from 3 distribution such as uniform(-50,50), standard cauchy
# turncated at -50 to 50, and t(df=30) turncateed at -50 to 50 to approximate the area under N(0,1) curve between -50 to 50
# In this problem we alos use two new libraries (only for histogram) 'numpy' and 'pylab'. 

import random
import math
import numpy as np
import pylab as P

# defining N(0,1) distribution between -50 to 50.
def infunc(x):                                                 
    I = (1/math.sqrt(2.0*math.pi))*math.exp(-float(x)**2/2.0)*(x>=-50.0)*(x<=50.0)
    return (I)
# --------------------------------------------------------------------------------------------------------------------------

#(a) here we generate uniform(-50,50) to approximate N(0,1) 

r = 5000                                 # number of estimation
mean = range(r)                          # defining mean variable to store mean values
for j in range(r):                       # initializing a for-loop
    n = 1000                             # a sample of size 1000
    fg = range(n)                        # a variable to store the two functions' ratios
    for i in range(n):                   # initializing another for-loop
        x = random.uniform(-50.0,50.0)   # generating uniform values
        fg[i] = infunc(x)/(1.0/100)      # ratio of N(0,1) and uniform(-50,50)
    mean[j] = sum(fg)/n                  # storing the mean of the ratios

# some syntaxes only applicable for histograms in 'canopy' program
#P.figure()
#P.hist(mean)
#P.show()

#---------------------------------------------------------------------------------------------------------------------------
#(b) here we generate standard cauchy turncated at -50 to 50 to approximate N(0,1) 

# defining a function to get the standard cauchy distribution. It takes an input k, the number values to be generated    
def rcauchy(k):
    c = math.tan(math.pi*(random.random() - .5))  # mathematical form to get standard cauchy from uniform(0,1)
    return (c)

r = 5000                                # number of estimation
mean = range(r)                         # defining mean variable to store mean values
for j in range(r):                      # initializing a for-loop
    n = 1000                            # a sample of size 1000
    fg = range(n)                       # a variable to store the two functions' ratios
    for i in range(n):                  # initializing another for-loop
        x = rcauchy(1)                  # generating standard cauchy
        
        fg[i] = infunc(x)/(1.0/(math.pi*(1+(x*(x>=-50.0)*(x<=50.0))**2))) # ratio of N(0,1) and turncated cauchy
    mean[j] = sum(fg)/n                 # storing the mean of the ratios

#P.figure()
#P.hist(mean)
#P.show()

#---------------------------------------------------------------------------------------------------------------------------
#(c)  here we generate t(30) turncated at -50 to 50 to approximate N(0,1) 

# defining a function to get the stdent t-distribution. it takes 'df' as degrees of freedom    
df = 30                                     # degrees of freedom
def student_t(df):                          # initializing the function
    z = random.gauss(0.0, 1.0)              # generating standard notmal values
    y = random.gammavariate(0.5*df, 2.0)    # generating chi-square ranodm values by gamma variate
    t = z / (math.sqrt(y/df))               # calculating t-distribution
    return(t)                               # returning the desired ouput


# generate t(30) turncated at -50 to 50 to approximate N(0,1) 
r = 5000                                    # number of estimation
mean = range(r)                             # defining mean variable to store mean values
for j in range(r):                          # initializing a for-loop
    n = 1000                                # a sample of size 1000
    fg = range(n)                           # a variable to store the two functions' ratios
    for i in range(n):                      # initializing another for-loop
        x = student_t(df)                   # generating t-random values
        
        T = (math.gamma((df+1)/2.0)/(math.sqrt(df*math.pi)*math.gamma(df/2.0)))*(1+(x*(x>-50.0)*(x<50.0))**2.0/df)**(-(df+1)/2.0)
                                            # getting turncated t-values by using t-pdf
        fg[i] = infunc(x)/T                 # # ratio of N(0,1) and turncated t-dist
    mean[j] = sum(fg)/n

P.figure()
P.hist(mean)
P.show()



#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################





