# -*- coding: utf-8 -*-
"""
Created on Thu May  3 17:28:38 2018

@author: sgmih
"""

#!/usr/bin/env python3

import sinwave
import msdplot
import sumplot
import matplotlib.pyplot as plt
import Sort_sum_time

"""
Sinewave plot
"""
sinwave.sinewave()

"""
Mass Spring Damper System
"""

msdplot.msdplot()

"""
Sum of ten samples from a uniform distribution from 0 to 1. 
Function ran 1000 times and store what it returns in a list. Plot the values in this list as a histogram
"""

i = 0
l = []
while i < 1000:
        s = np.random.uniform(0.0,1.0,10)
        l1 = sumplot.add(s)
        l.append(l1)
        i += 1     
x = l
plt.figure(3)
plt.hist(x, bins=100)
plt.title('Histogram for sum of 10 random uniformly distributed samples ')
plt.show()

 
"Time required to Sort and Sum a sample list"   

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
plt.figure(4)
plt.semilogx()
plt.plot(size, sort, 'r')
plt.title('Time required to sort sample lists')
plt.xlabel('No. of samples in the list')
plt.ylabel('Sorting time')
    
plt.figure(5)
plt.semilogx()
plt.plot(size, addition, 'g')
plt.title('Time required to calculate the sum of the samples in a list')
plt.xlabel('No. of samples in the list')
plt.ylabel('Summation time')
