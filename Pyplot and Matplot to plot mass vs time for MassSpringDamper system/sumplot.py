# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:56:13 2018

@author: sgmih
"""

#!/usr/bin/env python3

from math import *
import numpy as np
import matplotlib.pyplot as plt

def add(s):
    total = 0
    for x in s:
        total += x
    return total
        
if __name__ == '__main__':
    i = 0
    l = []
    while i < 1000:
        s = np.random.uniform(0.0,1.0,10)         
        l1 = add(s)
        l.append(l1)
        i += 1     
    plt.hist(l, bins=100)
    plt.show()
    
    
        