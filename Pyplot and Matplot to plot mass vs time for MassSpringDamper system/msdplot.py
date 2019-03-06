# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 09:36:53 2018

@author: sgmih
"""

from msd import*
import numpy as np
import matplotlib.pyplot as plt

def msdplot():
    smd = MassSpringDamper(m=10.0, k=10.0, c=1.0)
    state,t = smd.simulate(0.0, 1.0)
    x = [] 
    for s in state:
        x.append(s[0])
    fig = plt.figure()
    plt.plot(t,x)
    plt.title("Displacement v/s Time")
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    return fig

if __name__ == '__main__':
    msdplot()
    





