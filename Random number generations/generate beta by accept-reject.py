import random
import math
import numpy as np
import pylab as P

#====================================================================================================================
# Problem - 3
#-----------------------------------------------------------------------------------------------
# Generate Beta(2,2) by accept-reject algorithm
# in this case our g(x) is uniform(0,1) and f(x) is Beta(2,2)
n = 1000
k = 0                                  # counter for accepted simulations
j = 0                                  # counter for total no. of simulations
fx = 0                                 # initializing f(x) density
beta = []
fx_sum = 0                             # a variable to store the sum of Beta random values
fx_sq_sum = 0                          # another variable to store sum of squares
while k < n:                           # initializing a while loop, it will continue till k < n
        u = random.uniform(0, 1)       # generating a uniform random value
        j = j + 1
        gx = random.uniform(0, 1)      # generating another uniform random value from g(x)
        if u < gx*(1-gx):              # comapring f(x)/g(x)=gx*(1-gx) with uniform 
            k = k + 1
            fx = gx                    # setting f(x)=g(x) if u < gx*(1-gx)
            beta.append(fx)
#            print(fx)                 # print Beta random variates
            fx_sum = fx_sum + fx                     # sum of  Beta random values
            fx_sq_sum = fx_sq_sum + math.pow(fx, 2)  # sum of squares of Beta
#            print(k)
#print(j)
mean = fx_sum/n                                       # mean of the Beta sample
var = (fx_sq_sum - n*mean**2)/(n-1)                   # sample variance
print "beta sample mean of the sample is :" 
print mean
print "beat sample variance of the sample is :"
print var

#sample mean and variance are close to expected mean .5 and variance 0.05

# creating a beta histogram
P.figure()
P.hist(beta)
P.show()