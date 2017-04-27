import random
import math
import numpy as np
import pylab as P
====================================================================================================================
# Problem - 4
#--------------------------------------------------------------------------------------------------------------------
# Generate Gamma(5.5,2.5) by Whittaker's Method
n = 1000
alpha = 5.5                 # alpha and theta are two parameters of gamma
theta = 2.5
int_alpha = int(alpha)      # extracting integer part of the alpha
p = alpha - int_alpha
gamma = []
x2 = 0                              # intialize x2 variabele
x_sum = 0                           # a variable to store the sum of gamma random values
x_sq_sum = 0                        # another variable to store sum of squares
for i in range(n):                  # initializing a for loop
        x1 = 0                                       # initialize x1 variable
        for j in range(int_alpha):                   # initializing another for loop
                exp = random.expovariate(theta)      # generating a exponential random value
                x1 = x1 + exp                        # generating gamma(5,2.5) random variate
        u1 = random.uniform(0, 1)                    # generating a uniform random value
        u2 = random.uniform(0, 1)                    # generating another uniform random value
        s1 = u1**(1/p)
        s2 = u2**(1/(1-p))
        if (s1 + s2) <= 1:                           # if statement takes value if satisfy the condition
                    x2 = s1/(s1 + s2)
        u3 = random.uniform(0, 1)                    # generating another uniform random value
        x3 = -theta*x2*math.log(u3)                  # generating gamma(0.5,2.5) random variates
        x = x1 + x3
        gamma.append(x)
#        print(x)                                    # print gamma random variates
        x_sum = x_sum + x                            # sum of  gamma random values
        x_sq_sum = x_sq_sum + x**2                   # sum of squares of gamma
mean = float(x_sum)/n                                       # mean of the gamma sample
var = (x_sq_sum - n*mean**2)/(n-1)                   # sample variance
print "Gamma sample mean of the sample is:" 
print mean
print "Gamma sample variance of the sample is:" 
print var

#sample mean and variance are close to expected mean 2.2 and variance .88

# creating a gamma histogram
P.figure()
P.hist(gamma)
P.show()


