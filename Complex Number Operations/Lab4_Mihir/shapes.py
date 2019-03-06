# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:49:23 2018

@author: sgmih
"""

#!/usr/bin/env python3

from math import pi

class Circle():
    def __init__(self, r):
        if r > 0: 
            self.radius = r
        else:
            return None
        
    def area(self):
        return self.radius**2*pi
    
    def diameter(self):
        return self.radius*2
    
    def perimeter(self):
        return 2*pi*self.radius
    
class Rectangle():
    def __init__(self, l, w):
        if l > 0 and w > 0:
            self.length = l
            self.width = w
        else:
            return None
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    
if __name__ == '__main__':
    c = Circle(2)
    a = c.area()
    d = c.diameter()
    p = c.perimeter()
    print('{0:.2f}'.format(a))
    r = Rectangle(3,4)
    print(r.area())
    print(r.perimeter())
    
    
    
    
    
    
    
    
    
    
    