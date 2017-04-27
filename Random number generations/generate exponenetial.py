import random
import math
import numpy as np
import pylab as P

#==========================================================================================================
# 2(b) ----------------------------------------------------------------------------------------------------
# generating exponential(5) random sample of size 1000
n = 1000
theta = 5                                 # 'theta' is a exponential parameter
exp = []
exp_sum = 0                               # a variable to store the sum of exponential random values 
exp_sq_sum = 0                            # another variable to store the sum of squares
for i in range(n):                        # initialization of the for loop over n numbers
    u = random.uniform(0, 1)              # generating uniform random values
    e = -math.log(u)/theta                # using appropriate transformation to get exponential values
    exp.append(e)
#    print(e)                             # print exponential random variates
    exp_sum = exp_sum + e                 # sum of exponential random values
    exp_sq_sum = exp_sq_sum + e**2        # sum of squares of exponential
mean = exp_sum/n                          # mean of the exp. sample
var = (exp_sq_sum - n*mean**2)/(n-1)      # sample variance
print "Exponential sample mean of the sample is:" 
print mean
print "Exponential sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 0.2 and variance 0.04

# creating a exponential histogram
P.figure()
P.hist(exp)
P.show()