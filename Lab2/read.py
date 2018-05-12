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
#plt.plot(range(len(data)), data, 'r')
#plt.show()
#for i,datum in enumerate(data):
 #   print(i, datum)

     #with open("output_sensor_data.csv","w") as out_file:
         #for i in range(len(data)):

def mean_filter(l1,width):
    #raw = []
    #for x in range(len(l1)):
     #   raw.append(l1)
    #return raw
   # w = width // 2
    if width > 0 and width%2 != 0:
        #w = width // 2
        #raw = []
        #for x in range(len(l1)-2):
         #   raw.append(sum(l1[x]:l1[x+width]/width)
        #return raw
        raw=[]
        i=0
        while i+width <= len(l1):            
            y=l1[i:i+width]
            total_sum=sum(y)/width
            raw.append(total_sum)
            i+=1
        return(raw)
    else:
        return None
        
def median_filter(l1,width):
        raw_median = []
        j=0
        while j+width <= len(l1):            
            y=l1[j:j+width]
            total_sum= np.median(y)
            raw_median.append(total_sum)
            j+=1
        return(raw_median)
    
    
if __name__ == '__main__':
    l1 = generate_sensor_data()[:10]
    width = 3
    l2 = mean_filter(l1,width)
    l3 = median_filter(l1,width)
    print(l2,'raw')
    print(l3,'median')
    pass
    