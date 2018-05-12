# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 08:32:23 2018

@author: sgmih
"""

#!/usr/bin/env python3

def sum_i(l):
    if len(l) == 0:
        return 0
    else:
        s = 0
        for x in l:
            s = s + x
        return s

def sum_r(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_r(l[1:])


if __name__ == '__main__':
    l = [2,4,5]
    print(sum_i(l))
    print(sum_r(l))
    
    
    