import random
import math
import numpy as np
import pylab as P

#============================================================================================================
# 2(d) ------------------------------------------------------------------------------------------------------
# generating Normal(10,25) random sample of size 1000 by Box-Muller algorithm
n = 1000
mu = 10                            # mean of normal 
sigma = 5                          # standard deviation of normal
norm = []
normal_sum = 0                     # a variable to store the sum of normal random values
normal_sq_sum = 0                  # another variable to store sum of squares
for i in range(n):                 # initialization of the for loop over n numbers
    u1 = random.uniform(0, 1)      # generating a uniform random value
    u2 = random.uniform(0, 1)      # generating another uniform random value
    z1 = math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2) # using appropriate transformation to get z1 and z2 
    z2 = math.sqrt(-2*math.log(u1))*math.sin(2*math.pi*u2) # two standard normal values
    normal = mu + z1*sigma                                 # transformation  from standard normal to normal
    norm.append(normal)
#    print(normal)                                         # print normal random variates
    normal_sum = normal_sum + normal                       # sum of  normal random values
    normal_sq_sum = normal_sq_sum + normal**2              # sum of squares of normal
mean = normal_sum/n                                        # mean of the normal sample
var = (normal_sq_sum - n*mean**2)/(n-1)         # sample variance
print "Normal sample mean of the sample is:" 
print mean
print "Normal sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 10 and variance 25

# creating a normal histogram
P.figure()
P.hist(norm)
P.show()