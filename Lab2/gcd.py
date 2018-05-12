# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:48:12 2018

@author: sgmih
"""
#!/usr/bin/env python3

def gcd(a,b):
    if b == 0:
        return a
    else:
        if a > b:
            d = a/b
            if d == int:
                return b
            else:
                return gcd(b,a%b)
        if a < b:
            d = b/a
            if d == int:
                return a
            else:
                return gcd(a,b%a)
        
if __name__ == '__main__':
    print(gcd(45,20))
    
    