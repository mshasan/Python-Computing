import random
import math
import numpy as np
import pylab as P

#==============================================================================================================
# 2(e) --------------------------------------------------------------------------------------------------------
# generating Chisquare(5) random sample of size 1000
n = 1000
chisqu = []
chisq_sum = 0                           # a variable to store the sum of chisquare random values
chisq_sq_sum = 0                        # another variable to store sum of squares
for i in range(n):                      # initialization of the for loop over n numbers
    chi = []                            # setup an emplty list
    for j in range(5):                  # another for loop 
        u1 = random.uniform(0, 1)       # generating a uniform random value
        u2 = random.uniform(0, 1)       # generating another uniform random value
        z1 = math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2) # generating a standard normal value
        chi.append(z1**2)                   # standard normal square to get a value of 1 df chisquare
    chisq = float(sum(chi))                 # a value of chisquare with 5 df
    chisqu.append(chisq)
#    print chisq                             # print chi square random varites
    chisq_sum = chisq_sum + chisq           # sum of  chisquare random values
    chisq_sq_sum = chisq_sq_sum + chisq**2  # sum of squares of chisquare
mean = chisq_sum/n                          # mean of the chisquare sample
var = (chisq_sq_sum - n*mean**2)/(n-1)      # sample variance
print "Chisquare sample mean of the sample is:" 
print mean
print "Chisquare sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 5 and variance 10

# creating a chisquare histogram
P.figure()
P.hist(chisqu)
P.show()