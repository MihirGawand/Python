# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:09:05 2018

@author: sgmih
"""

#!/usr/bin/env python3
def close (a,b,c):
    if abs(a-b)<c:
        return True
    else: 
        return False
    
if __name__ == '__main__':
    z = close (1,3,2)
    print(z)