import random
import math
import numpy as np
import pylab as P
================================================================================================================
# 2(f) ----------------------------------------------------------------------------------------------------------
# Generating Binomial(100,.7) random sample of size 1000
n = 1000
p = .7                                # binomial probability
binom = []
bino_sum = 0                          # a variable to store the sum of chisquare random values
bino_sq_sum = 0                       # another variable to store sum of squares
for i in range(n):                    # initialization of the for loop over n numbers
    bino = 0                          # intialization a binomial variable
    z = 0                             # initial count of bournouli success
    for j in range(100):              # another for loop
        u = random.uniform(0, 1)      # generating a uniform random value
        z = 1 if u <= p else 0        # if uniform(0,1) is less then count increses by 1
        bino =  bino + z              # sum of bournoulli to get a binomial random value
    binom.append(bino)
#    print(bino)                      # print binomial random variates
    bino_sum = bino_sum + bino                       # sum of  binomial random values
    bino_sq_sum = bino_sq_sum + bino**2              # sum of squares of chisquare
mean = float(bino_sum)/n                             # mean of the Binomial sample
var = (bino_sq_sum - n*mean**2)/(n-1)                        # sample variance
print(bino_sq_sum)
print "Binomial sample mean of the sample is:" 
print mean
print "Binomial sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 70 and variance 21

# creating a binomial histogram
P.figure()
P.hist(binom)
P.show()