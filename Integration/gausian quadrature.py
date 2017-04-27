# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 3:  In this probelm we use "Gaussian Quadrature" to evaluate integral(a)
#----------------------------------------------------------------------------------------------------------------------------
# definig a function called 'Gauss-Legendre' for calculating weights and nodes. Here, 'a' and 'b' are lower and upper limit
# of the integral and 'n' is the no. of nodes and weights to be calculated. It calculates 1 extra values

def gaulegf(a, b, n):               # intitializing the function
  x = range(n+1) # x[0] unused      # defining two variables x and w for storing nodes and weights respectively 
  w = range(n+1) # w[0] unused
  eps = 3.0E-14                     # error tolerance level
  m = (n+1)/2
  xm = 0.5*(b+a)
  xl = 0.5*(b-a)
  for i in range(1,m+1):                        # initializing a foor-loop
    z = math.cos(3.141592654*(i-0.25)/(n+0.5))  # a mathematical formula used to calculate weights and nodes     
    while True:                                 # initializing while-loop, when 'if' condition saatisfied the loop will stop
      p1 = 1.0                                  # initializing two variables p1 and p2                                   
      p2 = 0.0
      for j in range(1,n+1):                    # initializing a for-loop
        p3 = p2
        p2 = p1
        p1 = ((2.0*j-1.0)*z*p2-(j-1.0)*p3)/j    # formula to calculate 'Gauss-Legendre' weight
      pp = n*(z*p1-p2)/(z*z-1.0)                # mathematical manipulation to get the desired result
      z1 = z
      z = z1 - p1/pp
      if abs(z-z1) <= eps:                      # an 'if' condition to stop the while-loop
          break

    x[i] = xm - xl*z                            # mathematical manipulation to make integral's range between - 1 to 1
    x[n+1-i] = xm + xl*z
    w[i] = 2.0*xl/((1.0-z*z)*pp*pp)             # finial weights
    w[n+1-i] = w[i]
  return x, w                                   # returning nodes and weights

n = 33                       
x,w = gaulegf(0, 1, 33)    # applying 'Gauss-Legendre' function to get nodes and weights               
#print 'nodes='
#print x
#print 'weights='
#print w

#---------------------------------------------------------------------------------------------------------------------------
# definig the integral given in (a) and we will use this function according to the instruction given in the problems

print 'Gaussian quadrature applied to the integral (a) for', n+1, 'nodes:'         # Printing what we do in this program
def infunc(x):                                                 
    I = (1/math.sqrt(2*math.pi))*math.exp(-float(x)**2/2)
    return (I)
#----------------------------------------------------------------------------------------------------------------------------

# definig our required function to calculate "Gaussian quadrature". where 'a' and 'b' are lower and upper limits of the
# integral,'infunc' is our desired function to be integrated,'weights' takes list of weight and 'nodes' takes list of nodes

def GaussQuad(a,b,infunc,weights,nodes):    # initializing the "Gauss quadrature" function              
    area = 0.0                              # initializing a variable 'area' under the curve
    for i in range(1, n+1):                 # initializing a for-loop to work over all weights and nodes
        area += w[i]*infunc(x[i])           # increment the variable by one step in the loop 
    print area                              # printing the area

# test the function        
GaussQuad(0,1,infunc,w,x)                   # applying our function

#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################


