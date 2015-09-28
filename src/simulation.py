#!/usr/bin/env python

import functions
import variables

import time
import numpy as np
from scipy.integrate import odeint
from operator import mul

#sizze of the vector
k = variables.k
#initial conditions set in variables.py
X_0 = variables.X_0
#the time vector 
t_vec = np.linspace(variables.t_0,variables.t_1,variables.N)

#the drivative function whose definitons are present in functions.py
def dX_dt(X, t ):
    derivative = np.zeros(k)
    for i in range(k):
        derivative[i] = functions.rhs_functions[i](X)
    return derivative

print "Simulation loaded..."

def simulate():
    result = []     #the array to store all results

    sim_start_time = time.time()

    _ops = reduce(mul,((p[1]-p[0])/variables.init_step for p in X_0))-1
    if _ops<=0:
        raise ValueError('Number of operations have to be greater than zero')
    X_0_point = [i[0] for i in X_0]
    _pos = k-1
    _inc = 0
    result.append(odeint(dX_dt, np.array(X_0_point), t_vec))
    while _inc < _ops:
        if X_0_point[_pos]==X_0[_pos][1]-variables.init_step:
            X_0_point[_pos]=X_0[_pos][0]
            _pos -= 1
        else:
            X_0_point[_pos] += variables.init_step
            _inc += 1
            _pos = k-1      #increment the innermost loop
            result.append(odeint(dX_dt, np.array(X_0_point), t_vec))
            
    sim_end_time = time.time()

    print "Simulation completed in ",sim_end_time - sim_start_time,"seconds."
    return result

