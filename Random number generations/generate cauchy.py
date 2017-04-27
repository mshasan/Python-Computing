import random
import math
import numpy as np
import pylab as P

#===========================================================================================================
# 2(c) -----------------------------------------------------------------------------------------------------
# generate standard cauchy(0,1) random sample of size 1000
n = 1000
cau = []
cauchy_sum = 0                         # a variable to store the sum of standard cauchy random values
cauchy_sq_sum = 0                      # another variable to store the sum of squares
for i in range(n):                     # initialization of the for loop over n numbers
    u = random.uniform(0, 1)           # generating uniform random value
    c = math.tan(math.pi*(u-.5))       # using appropriate transformation to get standard cauchy values
    cau.append(c)
    #print(c)                          # print standard cauchy random variates
    cauchy_sum = cauchy_sum + c             # sum of standard cauchy random values
    cauchy_sq_sum = cauchy_sq_sum + c**2    # sum of squares of standard cauchy
mean = cauchy_sum/n                         # mean of the cauchy sample
var = (cauchy_sq_sum - n*mean**2)/(n-1)     # sample variance
print "Cauchy sample mean of the sample is:" 
print mean
print "Cauchy sample variance of the sample is:" 
print var

#expected mean and vriance are undefined

# creating a standard cauchy histogram
P.figure()
P.hist(cau)
P.show()