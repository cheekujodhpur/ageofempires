#!/usr/bin/env python

import numpy as np

#What are our variables? Resources and population
X_model = ['food','wood','population']

#Needed to map variable names to indices
def describe(X, variable_name, value):
    X[X_model.index(variable_name)] = value


#Total Number of variables, + 1 to account for time
k = len(X_model) + 1

#the ndarray to store initial conditions
X_0 = np.zeros(k)

#initial time, does NOT assume to be 0
t_0 = 0.0       #USERDEF

#final time, anything greater than t_1
t_1 = 10.0      #USERDEF

#number of simulation points
N = 100
#check
if t_0 >= t_1:
    raise ValueError('Initial time cannot be greater than final time')

#assign the initial time at the end of the array
X_0[k-1] = t_0

describe(X, 'food', 2)          #USERDEF
describe(X, 'wood', 1)          #USERDEF
describe(X, 'population', 10)   #USERDEF

#flag OK
print "Initial conditions defined..."
