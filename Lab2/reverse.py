# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:05:23 2018

@author: sgmih
"""

#!/usr/bin/env python3

def reverse_r(l1):
    if len(l1) < 2:            
        return l1
    else:
        return [l1[-1]] + reverse_r(l1[:-1])
    
def reverse_i(l1):
    length = len(l1)
    new_l1 = [1]*length
    if len(l1) < 2:
        return l1  
    else:
        for i in l1:
            length = length - 1
            new_l1[length] = i
    return new_l1
           

if __name__ == '__main__':
    l1 = [2,2,3,4]
    l2 = reverse_r(l1)
    print(l2)
    l3 = reverse_i(l1)
    print(l3)    