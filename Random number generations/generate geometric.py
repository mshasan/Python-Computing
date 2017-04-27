import random
import math
import numpy as np
import pylab as P

#==================================================================================================================
# 2(g) ------------------------------------------------------------------------------------------------------------
# Geometric random sample of size 1000
n = 1000
p = .7                                  # probability of first success
lmbda = -math.log(1-p)                  # appropriate transformation to get exponential parameter
geom = []
geo_sum = 0                             # a variable to store the sum of geomertic random values
geo_sq_sum = 0                          # another variable to store sum of squares
for i in range(n):                      # initialization of the for loop over n numbers
    exp = random.expovariate(lmbda)     # generating a exponential random value with parameter lambda
    geo = int(exp) + 1                  # generating a geometric random value
    geom.append(geo)
#    print(geo)                         # print Geometric random variates
    geo_sum = geo_sum + geo             # sum of  geometric random values
    geo_sq_sum = geo_sq_sum + geo**2    # sum of squares of geometric
mean = float(geo_sum)/n                 # mean of the geometric sample
var = (geo_sq_sum - n*mean**2)/(n-1)    # sample variance
print "Geometric sample mean of the sample is:" 
print mean
print "Geometric sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 1.429 and variance 0.612

# creating a geometric histogram
P.figure()
P.hist(geom)
P.show()