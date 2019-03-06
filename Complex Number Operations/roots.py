# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:08:57 2018

@author: sgmih
"""

#!/usr/bin/env python3

import math
from complex import Complex

             
def roots(coeff):
    a = coeff[0]
    b = coeff[1]
    c = coeff[2]
    d = b**2 - (4*a*c)
    if d < 0:
        root1 = -b/(2*a)
        root2 = math.sqrt(-d)/(2*a)
        roots = (Complex(root1,root2), Complex(root1,-root2)) 
        return roots
    
    if d > 0:
        root1 = float(-b + math.sqrt(d))/ (2 * a)
        root2 = float(-b - math.sqrt(d))/ (2 * a)
        roots = (root1, root2)
        return roots
    elif d == 0:
        root1 = float(-b + math.sqrt(d))/ (2 * a)
        roots = (root1, 0)     

        
def evaluate(coeff, x):
    d = coeff
     
    if len(d) == 3:
        a = d[0]
        b = d[1]
        c = d[2]
        
        if isinstance(x,Complex):
            eqn = (a * x * x) + (b * x) + (c)
            return eqn 
            
        if isinstance(x,(float,int)):
            eqn = (a * x * x) + (b * x) + (c)
            return eqn
                       
        if len(x) == 2:
            x1 = x[0]
            x2 = x[1]
            
            x1 = (a * x1 * x1) + (b * x1) + (c)
            if isinstance(x1,Complex):
                x1.re = round(x1.re,2)
                x1.im = round(x1.im,2)
            elif isinstance(x1,float):
                x1 = round(x1,2)
            else:
                x1 = x1
            
            x2 = (a * x2 * x2) + (b * x2) + (c)
            if isinstance(x1,Complex):
                x2.re = round(x2.re,2)
                x2.im = round(x2.im,2)
            elif isinstance(x2,float):
                x2 = round(x2,2)
            else:
                x2 = x2
            
            return x1,x2
            
                         
    if len(d) == 4:
        a = d[0]
        b = d[1]
        c = d[2]
        d = d[3]
        
    
        if isinstance(x,Complex):
            eqn = (a * x * x * x) + (b * x * x) + (c * x) + d
            return eqn
        
        if isinstance(x,(float,int)):
            eqn = (a * x * x * x) + (b * x * x) + (c * x) + d
            return eqn
        
        if len(x) == 2:
            x1 = x[0]
            x2 = x[1]
            
            x1 = (a * x1 * x1 * x1) + (b * x1 * x1) + (c)
            if isinstance(x1,Complex):
                x1.re = round(x1.re,2)
                x1.im = round(x1.im,2)
            elif isinstance(x1,float):
                x1 = round(x1,2)
            else:
                x1 = x1
                
            x2 = (a * x2 * x2 * x2) + (b * x2 * x2) + (c)
            if isinstance(x1,Complex):
                x2.re = round(x2.re,2)
                x2.im = round(x2.im,2)
            elif isinstance(x2,float):
                x2 = round(x2,2)
            else:
                x2 = x2
            
            return x1,x2

        
#MAIN
if __name__ == '__main__':
    print(roots([1,2,3]))
    e = evaluate([1,2,3], roots([1,2,3]))
    print(e)
    
    """ 
    I have wrote a separate test code file for this complex.py named as test_complex which tests cases
    for both complex.py and roots.py. Please run that file which will show you the unittest module
    that I have written for both the codes
    
    Thank you,
    Mihir
    """"