# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 15:54:39 2018

@author: sgmih
"""

#!/usr/bin/env python3

import math


def estimate_pi():
    d = 1
    e = 0
    k = 0
    a = (2*math.sqrt(2))/9801
    while abs(d) >= 1e-15:
        b = factorial(4*k) * (1103 + (26390*k))
        c = ((factorial(k))**4) * (396**(4*k))
        d = (a*b)/c
        e = e + d
        k = k + 1
        return (1/e)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

print(estimate_pi())
        
        
        









if __name__ == '__main__':
    print(estimate_pi)