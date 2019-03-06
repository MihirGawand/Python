# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:29:00 2018

@author: sgmih
"""

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from math import pi

def sinewave():
    theta = np.arange(0.0, 4*pi, pi/10)
    amplitude = np.sin(theta)
    fig = plt.figure()
    plt.plot(theta, amplitude)
    plt.title('Sine wave')
    plt.xlabel('Theta')
    plt.ylabel('Amplitude = sin(theta)')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    return fig
    
if __name__ == '__main__':
    sinewave()