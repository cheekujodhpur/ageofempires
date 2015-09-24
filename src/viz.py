#!/usr/bin/env python

import numpy as np
import variables

#function to write results in a csv file to be used for plotting
def csv_out(result,outfile):
    #write headers
    for x in variables.X_model:
        outfile.write(x+',')
    outfile.write('time')   #time field
    outfile.write('\n')

    #write the data
    for i in result:
        for j in i:
            outfile.write(str(j)+',')
        outfile.write('\n')

#function to plot given fields
def plot_from_result():
    print "In Progress"
