# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:51:19 2018

@author: sgmih
"""

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from null_filter import *
from sensor import *

def mean_filter(l1):
    width = 3
    raw = []
    for x in range(len(l1)-2):
        raw.append((l1[x]+l1[x+1]+l1[x+2])/width)
    return raw


def var_mean_filter(l1,width):
    if width > 0 and width%2 != 0:
        raw_mean = []
        i=0
        while i+width <= len(l1):            
            y=l1[i:i+width]
            total_sum=sum(y)/width
            raw_mean.append(total_sum)
            i+=1
        return(raw_mean)
        
    else:
        return None
        
def median_filter(l1,width):
    if width > 0 and width%2 != 0:
        raw_median = []
        j=0
        while j+width <= len(l1):            
            y=l1[j:j+width]
            med = np.median(y)
            raw_median.append(med)
            j+=1
        return(raw_median)
    else:
        return None
    
    
if __name__ == '__main__':
    l1 = generate_sensor_data()  #raw sensor data
    l2 = mean_filter(l1)
    l3 = var_mean_filter(l1,5)
    l4 = median_filter(l1,3)
    print(l2,'mean')
    plt.plot(range(len(l2)),l2,'r')
    plt.show
    plt.plot(range(len(l3)),l3,'g')
    plt.show
    print(l3,'variable width mean')
    print(l4,'variable width median')
    plt.plot(range(len(l4)),l4,'b')
    plt.show
    
    l1 = apply_null_filter(data) #filtered sensor data
    l2 = mean_filter(l1)
    l3 = var_mean_filter(l1,5)
    l4 = median_filter(l1,3)
    print(l2,'mean')
    plt.plot(range(len(l2)),l2,'r')
    plt.show
    plt.plot(range(len(l3)),l3,'g')
    plt.show
    print(l3,'variable width mean')
    print(l4,'variable width median')
    plt.plot(range(len(l4)),l4,'b')
    plt.show
    pass
    