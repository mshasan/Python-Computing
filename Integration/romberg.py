# ----------------------------------------------------------------------------------------------------------------------------
# initializing two libraries "random" and "math" to generate random number and to use mathematical function, respectively

import random
import math


############################################################################################################################
#---------------------------------------------------------------------------------------------------------------------------
# Problem - 2:  In this probelm we use "Romberg Integration" to evaluate integrals. This is a complicated problem, that's
# why we define several function to make our program easier. Our required function's name is 'romint', however, we will use
# several functions such as 'trapezoid', 'difttrap','romberg_diff', and 'printresmat' inside the romint functions
#----------------------------------------------------------------------------------------------------------------------------


# defining another function to perform part of the trapezoidal rule to integrate a function. Assume that we call difftrap
# with all lower powers-of-2 starting with 1, and returns the summation of the new ordinates.
# It does _not_ multiply by the width of the trapezoids.  
# it also takes two limits 'a' and 'b', a function 'infunc', number of trapezoid to be calculated

def difftrap(a,b,infunc,numtraps):
    interval = [a,b]
    if numtraps==1:                             # an if condition, if satisfied then it will perform the following steps
                                                             # else it will go to the 'else' conditon
        return 0.5*(infunc(interval[0])+infunc(interval[1]))
    else:
        numtosum = numtraps/2
        h = float(interval[1]-interval[0])/numtosum          # calculation height of the trepedzoid
        lox = interval[0] + 0.5 * h                         # adjusting lower limit
        sum = 0.0
        for i in range(0, numtosum):                         # initializing a for loop to add functional values
            sum = sum + infunc(lox + i*h)
        return sum
# -----------------------------------------------------------------------------------------------------------------------------
# A function to compute the differences for the Romberg quadrature corrections, or calculating newRows.
# it takes a,b,and k, some integer values to define specific rows
   
def romberg_diff(b, c, k):
    tmp = 4.0**k
    return (tmp * c - b)/(tmp - 1.0)
#------------------------------------------------------------------------------------------------------------------------------
# a function to print the Romberg result matrix, or show into tabulated form
# it takes two limits 'a' and 'b', a function 'infunc', and result of the Romber integration

def printresmat(a,b,infunc,resmat):
    interval = [a,b]
    i = j = 0
    print 'Romberg integration of', `infunc`,                       # print name of the function
    print 'from', interval
    print ''
    print '%6s %9s %9s' % ('Steps', 'StepSize', 'Results')          # creating table's headlines
    for i in range(len(resmat)):                                        # these consequtive two for-loops inputing the 
        print '%6d %9f' % (2**i, (interval[1]-interval[0])/(i+1.0)),    # results into a tabulated form
        for j in range(i+1):
            print '%9f' % (resmat[i][j]),                               
        print ''
    print ''
    print 'The final result is', resmat[i][j],                          # print final result
    print 'after', 2**(len(resmat)-1)+1, 'function evaluations.'        # print the number of evulations needed
#-------------------------------------------------------------------------------------------------------------------------------
# Defining 'romint' to perform Romberg integratin. It returns the integral of a function.
# it takes two limits 'a' and 'b', a function 'infunc', maximum number of iteration 'm', error tolerance 'e', and 'show'
# show the triangular array of the intermediate results will be printed if show=1.
    
def romint(a,b,infunc,m,e=1.0E-7,show=0):
    interval = [a,b]
    i = n = 1
    intrange = interval[1] - interval[0]            # range between lower and upper linit
    ordsum = difftrap(a,b,infunc,n)                 # using a function defined above to get ordinates
    newI = intrange * ordsum
    resmat = [[newI]]                               # defining a variable to store all the results
    oldI = newI + e * 2.0
    while (abs(newI - oldI) > e) and m <= maxit:    # initializing while-loop to control error tolerance and iterations
        n = n * 2
        ordsum = ordsum + difftrap(a,b,infunc,n)    # again getting ordnates using predefined fnction
        resmat.append([])                           # a variable to store the results as vector
        resmat[i].append(intrange * ordsum / n)     # for each i creating vector
        for k in range(i):
            resmat[i].append(romberg_diff(resmat[i-1][k], resmat[i][k], k+1)) # using a predefined function differences for
                                                                              #the Romberg quadrature corrections
        newI = resmat[i][i]                             # new result
        oldI = resmat[i-1][i-1]                         # previous result
        i = i + 1                                       # forwarding by one step
        m=i
    if show: printresmat(a,b,infunc,resmat)             # if condtion to show the result into tabulated form
    return newI


#---------------------------------------------------------------------------------------------------------------------------
# definig a function given in (a) and we will use this function according to the instruction given in the problems
#2(a): Romberg Integration rule for the integral(a)

def infunc(x):                                             # the given integral to be evaluated        
    I = (1/math.sqrt(2*math.pi))*math.exp(-float(x)**2/2)
    return (I)

# test the function
# interpreter reads a source file, it executes all of the code found in it before executing the code

if __name__ == '__main__':
    print ''
    maxit=20
    r = romint(0.0,1.0,infunc,maxit,show=1)     # applying 'Romberg integration' function
    print ''
    
#---------------------------------------------------------------------------------------------------------------------------
# 2(b): Romberg Integration rule for the integral(b)


def infunc(x):
    I = math.sin(2*x)**2/x**2
    return(I)

# test the function
# interpreter reads a source file, it executes all of the code found in it before executing the code

if __name__ == '__main__':
    print ''
    maxit=20
    r = romint(math.pi,1.5*math.pi,infunc,maxit,show=1)  # applying 'Romberg integration' function
    print ''

# Romberg takes less computation than trapedodial rule    
#---------------------------------------------------------------------------------------------------------------------------
############################################################################################################################


