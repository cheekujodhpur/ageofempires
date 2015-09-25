#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import variables
import functions

#function to write results in a csv file to be used for plotting
#def csv_out(result,outfile):
#    #write headers
#    for x in variables.X_model:
#        outfile.write(x+',')
#    outfile.write('time')   #time field
#    outfile.write('\n')
#
#    #write the data
#    for i in result:
#        for j in i:
#            outfile.write(str(j)+',')
#        outfile.write('\n')

#function to plot given field against time
#def var_vs_time(result,variable):
#    plt.plot(result[:,variables.k-1],result[:,functions.map_vars(variable)])
#    plt.show()

#function to plot given field against given field
#def var_vs_var(result,variable_x,variable_y):
#    plt.plot(result[:,functions.map_vars(variable_x)],result[:,functions.map_vars(variable_y)])
#    plt.show()


#function to plot two fields, for varying initial conditions
def phase_2D(results,variable_x,variable_y,ax_xlim=None,ax_ylim=None):
    fig,ax = plt.subplots()

    #define axis limits if specified
    if(ax_xlim):
        ax.set_xlim(ax_xlim)
    if(ax_ylim):
        ax.set_ylim(ax_ylim)
        
    for result in results:
        ax.plot(result[:,functions.map_vars(variable_x)],result[:,functions.map_vars(variable_y)])
    plt.show()

#function to plot three fields, for varying initial conditions
def phase_3D(results,variable_x,variable_y,variable_z,ax_xlim=None,ax_ylim=None,ax_zlim=None):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    #define axis limits if specified
    if(ax_xlim):
        ax.set_xlim(ax_xlim)
    if(ax_ylim):
        ax.set_ylim(ax_ylim)
    if(ax_zlim):
        ax.set_zlim(ax_zlim)
        
    for result in results:
        ax.plot(result[:,functions.map_vars(variable_x)],result[:,functions.map_vars(variable_y)],zs=result[:,functions.map_vars(variable_z)])
    plt.show()

#function to plot given field against time, for varying initial conditions
#def var_vs_time_multi(results,variable):
#    fig,ax = plt.subplots()
#    for result in results:
#        ax.plot(result[:,variables.k-1],result[:,functions.map_vars(variable)])
#    plt.show()


