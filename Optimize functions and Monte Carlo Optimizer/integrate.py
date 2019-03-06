# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:57:33 2018

@author: Mihir Gawand
"""
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import integrate


def funct(x):
    return x**2


def integrate_mc(f,bounds,n):
    
    x1,x2 = bounds
    X = np.linspace(x1,x2,n)
    y1 = 0
    y2 = max((f(X))) + 1
    area = (x2-x1)*(y2-y1)
    print("Area:", area )
    check = []
    xs = []
    ys = []
    for i in range(n):
        x = np.random.uniform(x1,x2,1)
        xs.append(x)
        y = np.random.uniform(y1,y2,1)
        ys.append(y)
        if abs(y)>abs(f(x)) or y<0:
            check.append(0)
        else:
            check.append(1)
    return np.mean(check)*area

def plots(f , bounds):
    
    lower, upper = bounds     
    n_vals = (10,50,100,500,1000,5000)
    inte = integrate.quad(f, lower, upper)
    known_val = inte[0]
    
    lists={"Monte Carlo": []}

    for i in n_vals:
        
        lists["Monte Carlo"].append(known_val-integrate_mc(f,bounds,i)) 
              
    d=pd.DataFrame(lists)
    d.index=n_vals
    ax = d.plot(lw=2, colormap='jet', marker='.', markersize=5, title='Monte Carlo plot')
    ax.set_xlabel('Number of runs')
    ax.set_ylabel('Error')

  
if __name__ == '__main__':
    print(integrate_mc(funct,(1,10),100))
    
    b = plots(funct,(0,4))
    print(b)
    

        
        
    
    
    
    