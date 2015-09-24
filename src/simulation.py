#!/usr/bin/env python

import functions
import variables

import time
import numpy as np
from scipy.integrate import odeint

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
    sim_start_time = time.time()
    result = odeint(dX_dt, X_0, t_vec)
    sim_end_time = time.time()

    print "Simulation completed in ",sim_end_time - sim_start_time,"seconds."
    return result

