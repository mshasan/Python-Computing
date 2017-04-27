# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math

#----------------------------------------------------------------------------------------------------------------------------
# Problem - 1:  In this problem we use "Extended trapeddodial rule" to evaluate 3 integrals
#----------------------------------------------------------------------------------------------------------------------------
# Extended trapedodial rule for the integral(a). In this problem we define a function named "trapint", which takes two
# limits 'a' and 'b', a function 'infunc' given in the problem, maximum number of iterations 'nmax', and error tolerance 'e'. 

def trapint(a,b,infunc,nmax,e):                         # defning a function 'infunc'
    n = 2                                               # initializing iteration identifying variable
    diff = 1.0                                            # initializing a vriable to detect error between to iterations
    oldI = 0.0                                            # initializing another variable
    
    I1 = (b-a)*(float(1)/2*infunc(a) + float(1)/2*infunc(b))                # 1st stage integration
    print 'iteration='+repr(1)+', Ivalue='+repr(I1)+', error='+repr(1000)   # print 1st stage integration's output and error
    
    newI = I1                                        # initializing a new variable to store integration in every iteration
    while diff >= e*abs(oldI) and n <= nmax:	     # starting while loop runs untill the given conditions are satisfied
            oldI = newI				

            A = 0                                                       # another new variable
            for i in range(1, 2**(n-2)+1):                              # starting for-loop takes values from t to 2^(n-1)
                    A = A + infunc(a+float((2*i-1)*(b-a))/(2**(n-1)))

            newI = float(1)/2*oldI + (float(b-a))/(2**(n-1))*A      # storing output from for-loop result
            diff = abs(newI - oldI)                                 # calculating error between two consequtive integration
            n = n + 1                                               # counting no. of iteration
            
            print 'iteration='+repr(n-1)+', Ivalue='+repr(newI)+', error='+repr(diff) # print all the desired outputs
    print(newI)                   # print the final result of the integration
    


#---------------------------------------------------------------------------------------------------------------------------
# definig a function given in (a) and we will use this function according to the instruction given in the problems
#1(a): Extended trapedodial rule for the integral(a)

print 'Trapezoidal Rule applied to integral a:'             # Printing what we do in this program
def infunc(x):                                                 
    I = (1/math.sqrt(2.0*math.pi))*math.exp(-float(x)**2/2.0)
    return (I)

#test the function
trapint(0.0,1.0,infunc,20,10**(-6))                         # Applyting the "tranpint" function that we defined before

#---------------------------------------------------------------------------------------------------------------------------
# 1(b): Extended trapedodial rule for the integral(b)

print 'Trapezoidal Rule applied to integral b:'        # Printing what we do in this program
def infunc(x):
    I = math.sin(2.0*x)**2/x**2.0
    return(I)

#test the function
trapint(math.pi,1.5*math.pi,infunc,20,10**(-6))         # Applyting the "tranpint" function that we defined before


#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################

