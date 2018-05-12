# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:50:10 2018

@author: sgmih
"""

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from random import *
import time

def sort_time(s):
    start = time.clock()
    s.sort()
    return time.clock() - start

def add(s):
    start = time.clock()
    np.sum(s)
    return time.clock() - start
    
#def add_time():
#    
#    
if __name__ == '__main__':
    sort = []
    addition = []
    size = []
    i = 1
     
    while i <= 1000000:
        s = np.random.random_sample((i,))
        s1 = sort_time(s)
        sort.append(s1)
        a1 = add(s)
        addition.append(a1)
        size.append(i)
        i = i*10
    print(size)
    
    print(sort)
    print(addition)
    fig = plt.figure()
    plt.figure(0)
    plt.semilogx()
    plt.plot(size, sort, 'r')
    
    plt.figure(1)
    plt.semilogx()
    plt.plot(size, addition, 'g')
    
    
#    s = np.random.random_sample((10,))
#    s2 = sort_time(s)
#    a2 = add(s)
#    sort.append(s2)
#    addition.append(a2)
#    
#    s = np.random.random_sample((100,))
#    s3 = sort_time(s)
#    a3 = add(s)
#    sort.append(s3)
#    addition.append(a3)
#    
#    s = np.random.random_sample((1000,))
#    s4 = sort_time(s)
#    a4 = add(s)
#    sort.append(s4)
#    addition.append(a4)
#    
#    s = np.random.random_sample((10000,))
#    s5 = sort_time(s)
#    a5 = add(s)
#    sort.append(s5)
#    addition.append(a5)
#    
#    s = np.random.random_sample((100000,))
#    s6 = sort_time(s)
#    a6 = add(s)
#    sort.append(s6)
#    addition.append(a6)
#    
#    s = np.random.random_sample((1000000,))
#    s7 = sort_time(s)
#    a7 = add(s)
#    sort.append(s7)
#    addition.append(a7)
    
   
    
    
#        i += 1     
#    print(l)