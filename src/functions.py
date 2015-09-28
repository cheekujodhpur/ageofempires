#!/usr/bin/env python

import numpy as np
import variables

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
alpha1 = 0.3    #USERDEF
alpha2 = 0.7    #USERDEF
beta = 0.2    #USERDEF
gamma = 0.5    #USERDEF
delta = 0.5     #USERDEF

def f_area(X):   #USERDEF
    if(X[area]<100):
        return (X[popn]-(alpha1+alpha2)*X[area])
    else:
        return 0
def f_food(X):   #USERDEF
    return alpha2*X[area]-X[popn]
def f_popn(X):   #USERDEF
    return gamma*X[popn]-delta*(X[popn]-X[food])

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
