import random
import math
import numpy as np
import pylab as P
#=======================================================================================================
# Probelm - 2
# 2(a) -------------------------------------------------------------------------------------------------
# generating uniform(0,1) random sample of size 1000
n = 1000                                # 'n' is sample size or number of iteration for all problems
a = 7**5                                # 'a' is called multiplier takes integer value
m = 2**31 - 1                           # 'm' is mudulas
xu = [10]                                # Setup a list with inital value 10
for i in range(n):                      # initialization of the for loop over n numbers
    xu.append(a*xu[i-1]%m)                # Append to store values sequently
u = [float(y)/m for y in xu]             # uniform random values
#print(u)                               # print uniform random variates
mean = float(sum(u))/n                  # mean of the sample
var = (sum([z**2 for z in u]) - n*mean**2)/(n-1)          # sample variance 
print "Uniform sample mean of the sample is:" 
print mean
print "Uniform sample variance of the sample is:" 
print var

# sample mean and variance are close to expected mean 0.5 and variance .0833

#creating a uniform histogram
P.figure()
P.hist(xu)
P.show()
