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
food2 = map_vars('food2')
popn2 = map_vars('population2')
area2 = map_vars('area2')

#additional parameters
alpha = 0.1     #USERDEF
beta = 0.1     #USERDEF

def f_area(X):   #USERDEF
    return X[area]*X[popn]*(-X[area]+alpha*X[popn])
def f_popn(X):   #USERDEF
    return X[area]*X[popn]*X[food]*(-X[food]+beta*X[popn])*(-X[area]+alpha*X[popn])-X[area2]*X[food2]*X[popn]+X[area]*X[food]*X[popn2]
def f_food(X):   #USERDEF
    return X[popn]*(-X[food]+beta*X[popn])*(-X[area]+alpha*X[popn])
def f_area2(X):   #USERDEF
    return X[area2]*X[popn2]*(-X[area2]+alpha*X[popn2])
def f_popn2(X):   #USERDEF
    return X[area2]*X[popn2]*X[food2]*(-X[food2]+beta*X[popn2])*(-X[area2]+alpha*X[popn2])+X[area2]*X[food2]*X[popn]-X[area]*X[food]*X[popn2]
def f_food2(X):   #USERDEF
    return X[popn2]*(-X[food2]+beta*X[popn2])*(-X[area2]+alpha*X[popn2])

#dummy function which gives derivative of time, with respect to time
def time(X):
    return 1

#make sure to append all the functions you define
rhs_functions.append(f_popn)     #USERDEF
rhs_functions.append(f_food)     #USERDEF
rhs_functions.append(f_area)     #USERDEF
rhs_functions.append(f_popn2)     #USERDEF
rhs_functions.append(f_food2)     #USERDEF
rhs_functions.append(f_area2)     #USERDEF

rhs_functions.append(time)

if len(rhs_functions)!=variables.k:
    raise ValueError("Number of functions don't match the number of variables")

print "Functions defined..."
