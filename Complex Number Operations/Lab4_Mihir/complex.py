# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:11:10 2018

@author: sgmih
"""

#!/usr/bin/env python3

import cmath

class Complex():
    def __init__(self, r = 0, i = 0):
        self.re = r
        self.im = i

  
    def __str__(self):
        if self.im < 0:
            return '({0} '.format(self.re) + '- {0}i)'.format(abs(self.im))        
        else:        
            return '({0} '.format(self.re) + '+ {0}i)'.format(self.im)
   

    def __add__(self,other):
        if isinstance(other,(float,int)):
            return Complex(self. re + other,
                           self.im)
        else:
            return Complex(self. re + other.re,
                           self.im + other.im)  
            
            
    def __radd__(self,other):
        return self + other
    
            
    def __sub__(self,other):
        if isinstance(other,(float,int)):
            return Complex(self.re - other, self.im)
        else:
            return Complex(self.re - other.re,
                           self.im - other.im)
            
            
    def __rsub__(self,other):
        return Complex(other) - self

        
if __name__ == '__main__':
    pass
    
    
    