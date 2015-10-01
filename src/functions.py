#!/usr/bin/env python

import numpy as np
import variables
import math

#the functions which define evolution of the state
rhs_functions = []

def map_vars(name):
    if(name=='time'):
        return variables.k-1
    else:
        return variables.X_model.index(name)

#dummy
food = map_vars('food')
popn = map_vars('population')
area = map_vars('area')

#additional parameters

#land portion used to live
alpha1 = 0.3    #USERDEF
#land portion used for cultivation
alpha2 = 0.7    #USERDEF
beta = 0.2    #USERDEF
gamma = 0.5    #USERDEF
delta = 0.5     #USERDEF

#assumption that 1 unit of population needs one unit of area
#assumption that 1 couple gives 0.25 child(ren) per year

def f_area(X):   #USERDEF
    #if there are more people than we have to make them live
    if int(X[popn])>int(alpha1*X[area]):
        #if they can't even survive without it, increase by the surplus, rapidly
        if int(X[popn])>int(X[area]):
            return X[popn]-X[area]
        #otherwise they only need increase at the rate of increase
        else:
            return max(f_popn(X),0)
    else:
        return 0
def f_food(X):   #USERDEF
    return alpha2*X[area]-X[popn]
def f_popn(X):   #USERDEF
    return 1.125*(X[food]) - X[popn]

#dummy function which gives derivative of time, with respect to time
def time(X):
    return 1

#make sure to append all the functions you define
rhs_functions.append(f_popn)     #USERDEF
rhs_functions.append(f_food)     #USERDEF
rhs_functions.append(f_area)     #USERDEF

rhs_functions.append(time)

if len(rhs_functions)!=variables.k:
    raise ValueError("Number of functions don't match the number of variables")

print "Functions defined..."
