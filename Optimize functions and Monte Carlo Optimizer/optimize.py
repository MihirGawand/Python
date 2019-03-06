# -*- coding: utf-8 -*-

"""
Created on Fri Jun  1 09:44:20 2018

@author: sgmih
"""

#!/usr/bin/env python3

import numpy as np
import random
import numpy as np
import scipy
from scipy.optimize import minimize_scalar
import pandas as pd

        
def optimize_step(f,bounds,n):
    
    lower,upper = bounds
    x1 = 0
    l = 0
    output = []
    
    while lower <= upper:
        x = f(lower)
        output.append(x)
        if x > x1:
            x1 = x
            l = lower
        lower = lower + n
    return l                           #returns the x value that gives the maximum output
          
def optimize_random(f,bounds,n):
    
    lower,upper = bounds
    samples = np.random.uniform(lower,upper,n)
    xmax = 0
    z = 0
    for y in range(len(samples)):
        x = f(samples[y])
        if x > xmax:
            xmax = x
            z = samples[y]
        else:
            pass
    return z                      #returns the x value that gives the maximum output
  
def minim_scalar(f,bounds,n):
    lower,upper = bounds
    opt = minimize_scalar(lambda x: -f(x),bounds=(lower,upper),method='bounded',options={'maxiter':n})
    return opt.x                  #returns the x value that gives the optimum output as calculated by the built-in optimizer

def funct1(x):
    return x**2

def funct2(x):
    return x**3 - (4*x**2) + (6*x) + 5

def funct3(x):
    return((1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2)) 
    

    
    
if __name__ == '__main__':
    s = funct1(2)    
    
    n_list = [5,10,15,20,25,50,75,100,200]
    n = 2
    a = optimize_step(funct3,(1,10),n)
    print(a)
    b = optimize_random(funct3,(1,10),n)
    print(b)
    c = minim_scalar(funct3,(1,10),30)
    print(c)
    
    list_funct1 = {"Step1" : [], "Random1" : [], "Scalar1" : []}
    
    for i in n_list: 
        list_funct1["Step1"].append(abs(optimize_step(funct1,(0,1000),i)-optimize_step(funct1,(0,1000),i)))
        list_funct1["Random1"].append(abs(optimize_random(funct1,(0,1000),i)-optimize_step(funct1,(0,1000),i)))
        list_funct1["Scalar1"].append(abs(minim_scalar(funct1,(0,1000),i)-optimize_step(funct1,(0,1000),i)))
        
    
    d = pd.DataFrame(list_funct1)
    d.index = n_list
    ax = d.plot(lw = 2, colormap = 'jet', marker ='.', markersize = 5, title = 'Easy Function funct1')
    ax.set_xlabel('Number of runs')
    ax.set_ylabel('Error')
    
    list_funct2 = {"Step2" : [], "Random2" : [], "Scalar2" : []}
    
    for i in n_list:
        list_funct2["Step2"].append(abs(optimize_step(funct2,(0,1000),i)-optimize_step(funct2,(0,1000),i)))
        list_funct2["Random2"].append(abs(optimize_random(funct2,(0,1000),i)-optimize_step(funct2,(0,1000),i)))
        list_funct2["Scalar2"].append(abs(minim_scalar(funct2,(0,1000),i)-optimize_step(funct2,(0,1000),i)))
        
        
    d = pd.DataFrame(list_funct2)
    d.index = n_list
    ax = d.plot(lw = 2, colormap = 'jet', marker ='.', markersize = 5, title = 'Hard Function funct2')
    ax.set_xlabel('Number of runs')
    ax.set_ylabel('Error')
        
    list_funct3 = {"Step3" : [], "Random3" : [], "Scalar3" : []}
    
    for i in n_list:
        list_funct3["Step3"].append(abs(optimize_step(funct3,(0,1000),i)-optimize_step(funct3,(0,1000),i)))
        list_funct3["Random3"].append(abs(optimize_random(funct3,(0,1000),i)-optimize_step(funct3,(0,1000),i)))
        list_funct3["Scalar3"].append(abs(minim_scalar(funct3,(0,1000),i)-optimize_step(funct3,(0,1000),i)))
        
        
    d = pd.DataFrame(list_funct3)
    d.index = n_list
    ax = d.plot(lw = 2, colormap = 'jet', marker ='.', markersize = 5, title = 'Harder Function funct3')
    ax.set_xlabel('Number of runs')
    ax.set_ylabel('Error')
        
        
    
    
    
    
    
    