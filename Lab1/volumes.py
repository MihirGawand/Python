# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:09:05 2018

@author: sgmih

Calculates the cylinder and torus volume by taking appropriate values
"""

#!/usr/bin/env python3
import math
def cylinder_volume (radius,height):
    if type(radius) == int or type (radius) == float:
        if type(height) == int or type (height) == float:
             if radius > 0:
                 if height > 0:
                    Vol_of_cylinder = (math.pi * (radius ** 2) * height)
                    return Vol_of_cylinder
    else:
        return None

def torus_volume (r,R):
    if type(r) == int or type (r) == float:
        if type(R) == int or type (R) == float:
             if R > 0:
                 if r > 0 and r < R:
                    Vol_torus = 0.25*(math.pi**2)*(r+R)*((R-r)**2)
                    return Vol_torus
    else:
        return None
    
if __name__ == '__main__':
    x = cylinder_volume(3,1)
    y = torus_volume(2,3)
    print(x)
    print(y)
