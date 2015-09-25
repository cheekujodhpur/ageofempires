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

def f(X):   #USERDEF
    return X[map_vars('wood')]*(1-X[map_vars('food')]**2)
def g(X):   #USERDEF
    return 1-X[map_vars('wood')]**2
def h(X):   #USERDEF
    return 0.5*X[map_vars('food')]

#dummy function which gives derivative of time, with respect to time
def time(X):
    return 1

#make sure to append all the functions you define
rhs_functions.append(f)     #USERDEF
rhs_functions.append(g)     #USERDEF
rhs_functions.append(h)     #USERDEF

rhs_functions.append(time)

if len(rhs_functions)!=variables.k:
    raise ValueError("Number of functions don't match the number of variables")

print "Functions defined..."
