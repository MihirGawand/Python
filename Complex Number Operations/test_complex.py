# -*- coding: utf-8 -*-
"""
This code tests the functions in both complex.py and roots.py

"""

import unittest
import cmath
from complex import Complex
from complex import sqrt
from roots import roots
from roots import evaluate

class TestComplex(unittest.TestCase):
    
    def test_add(self):
        
    #when both the variables are complex    
        a = Complex(5,10)
        b = Complex(2,5)
        result = (a + b)
        c = Complex(7,15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
         
        a = Complex(-5,10)
        b = Complex(2,5)
        result = a + b
        c = Complex(-3,15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,-10)
        b = Complex(2,5)
        result = a + b
        c = Complex(7,-5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = Complex(-2,5)
        result = a + b
        c = Complex(3,15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = Complex(2,-5)
        result = a + b
        c = Complex(7,5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = Complex(2,5)
        result = a + b
        c = Complex(-3,-5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = Complex(-2,-5)
        result = a + b
        c = Complex(3,5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = Complex(-2,-5)
        result = a + b
        c = Complex(-7,-15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = Complex(0,-5)
        result = a + b
        c = Complex(-5,-15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = Complex(2.5,-5.5)
        result = a + b
        c = Complex(-2.5,-15.5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
      #when only one variable is complex
        a = Complex(5,10)
        b = 2
        result = a + b 
        c = Complex(7,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = -2
        result = a + b 
        c = Complex(3,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = 2.5
        result = a + b 
        c = Complex(7.5,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = -2.5
        result = a + b 
        c = Complex(2.5,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        #reverse add
        a = Complex(5,10)
        b = 2.5
        result = b + a 
        c = Complex(7.5,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
    def test_sub(self):
        #when both the values are complex
        a = Complex(5,10)
        b = Complex(2,5)
        result = (a - b)
        c = Complex(3,5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = Complex(2,-5)
        result = (a - b)
        c = Complex(3,15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
           
        a = Complex(5,-10)
        b = Complex(2,5)
        result = (a - b)
        c = Complex(3,-15)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,-10)
        b = Complex(2,-5)
        result = (a - b)
        c = Complex(3,-5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = Complex(-2,-5)
        result = (a - b)
        c = Complex(-3,-5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = Complex(2.5,5.5)
        result = (a - b)
        c = Complex(2.5,4.5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        #when only variable is complex
        a = Complex(5,10)
        b = 2
        result = (a - b)
        c = Complex(3,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = -2.5
        result = (a - b)
        c = Complex(7.5,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-5,-10)
        b = 2
        result = (a - b)
        c = Complex(-7,-10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        #reverse add
        a = Complex(-5,-10)
        b = 2
        result = (b - a)
        c = Complex(7,10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(5,10)
        b = 2.5
        result = (b - a)
        c = Complex(-2.5,-10)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
    def test_mul(self):
        
        #when both the variables are complex
        a = Complex(1,4)
        b = Complex(5,1)
        result = (a * b)
        c = Complex(1,21)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-2,5)
        b = Complex(1,-3)
        result = (a * b)
        c = Complex(13,11)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(3,4)
        b = Complex(5,-2)
        result = (a * b)
        c = Complex(23,14)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(1,4)
        b = Complex(0,0)
        result = (a * b)
        c = Complex(0,0)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-3,-4)
        b = Complex(-5,-2)
        result = (a * b)
        c = Complex(7,26)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        #when only value is a complex variable
        a = Complex(1,4)
        b = 2
        result = (a * b)
        c = Complex(2,8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(1,4)
        b = -2
        result = (a * b)
        c = Complex(-2,-8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-1,-4)
        b = 2
        result = (a * b)
        c = Complex(-2,-8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-1,-4)
        b = -2
        result = (a * b)
        c = Complex(2,8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        #reverse multiply
        a = Complex(1,4)
        b = 2
        result = (b * a)
        c = Complex(2,8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(1,4)
        b = -2
        result = (b * a)
        c = Complex(-2,-8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-1,-4)
        b = -2
        result = (b * a)
        c = Complex(2,8)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        
    def test_truediv(self):
        
        #when both the values are complex variables
        a = Complex(3,2)
        b = Complex(4,-3)
        result = (a/b)
        c = Complex(0.24,0.68)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(4,5)
        b = Complex(2,6)
        result = (a/b)
        c = Complex(0.95,-0.35)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(2,-1)
        b = Complex(-3,6)
        result = (a/b)
        c = Complex(-4/15,-1/5)
        self.assertEqual(result.re, c.re)
        self.assertEqual(result.im, c.im)
        
        a = Complex(-6,-3)
        b = Complex(4,6)
        result = (a/b)
        c = complex(-6,-3)/complex(4,6)
        self.assertEqual(result.re, c.real)
        self.assertEqual(result.im, c.imag)
        
        a = Complex(-6,-3)
        b = Complex(-4,-6)
        result = (a/b)
        c = complex(-6,-3)/complex(-4,-6)
        self.assertEqual(result.re, c.real)
        self.assertEqual(result.im, c.imag)
        
        #when only one value is complex
        a = Complex(3,2)
        b = 5
        result = (a/b)
        c = complex(3,2)/5
        self.assertEqual(result.re, c.real)
        self.assertEqual(result.im, c.imag)
        
        a = Complex(-3,-2)
        b = 5
        result = (a/b)
        c = complex(-3,-2)/5
        self.assertEqual(result.re, c.real)
        self.assertEqual(result.im, c.imag)
        
        a = Complex(-3,-2)
        b = -5
        result = (a/b)
        c = complex(-3,-2)/-5
        self.assertEqual(result.re, c.real)
        self.assertEqual(result.im, c.imag)
        
        #reverse divison
        a = Complex(3,2)
        b = 5
        result = (b/a)
        result.re = round(result.re,2)
        result.im = round(result.im,2)
        c = 5/complex(3,2)
        dreal = round(c.real,2)
        dimag = round(c.imag,2)
        self.assertEqual(result.re, dreal)
        self.assertEqual(result.im, dimag)
        
        a = Complex(3,-2)
        b = 5
        result = (b/a)
        result.re = round(result.re,2)
        result.im = round(result.im,2)
        c = 5/complex(3,-2)
        dreal = round(c.real,2)
        dimag = round(c.imag,2)
        self.assertEqual(result.re, dreal)
        self.assertEqual(result.im, dimag)
        
        
        a = Complex(-3,-2)
        b = -5
        result = (b/a)
        result.re = round(result.re,2)
        result.im = round(result.im,2)
        c = -5/complex(-3,-2)
        dreal = round(c.real,2)
        dimag = round(c.imag,2)
        self.assertEqual(result.re, dreal)
        self.assertEqual(result.im, dimag)
        
        
    def test_sqrt(self):
        
        a = Complex(3,2)
        a = sqrt(a)
        b = complex(3,2)
        b = cmath.sqrt(b)
        self.assertEqual(a.re,b.real)
        self.assertEqual(a.im,b.imag)
        
        a = Complex(-3,-2)
        a = sqrt(a)
        b = complex(-3,-2)
        b = cmath.sqrt(b)
        self.assertEqual(a.re,b.real)
        self.assertEqual(a.im,b.imag)
        
        a = Complex(3,0)
        a = sqrt(a)
        b = complex(3,0)
        b = cmath.sqrt(b)
        self.assertEqual(a.re,b.real)
        self.assertEqual(a.im,b.imag)
        
        a = Complex(0,3)
        a = sqrt(a)
        a.re = round(a.re,2)
        a.im = round(a.im,2)
        b = complex(0,3)
        b = cmath.sqrt(b)
        breal = round(b.real,2)
        bimag = round(b.imag,2)
        self.assertEqual(a.re,breal)
        self.assertEqual(a.im,bimag)
        
    def test_neg(self):
        
        a = Complex(3,2)
        a = -a
        b = Complex(-3,-2)
        self.assertEqual(a.re,b.re)
        self.assertEqual(a.im,b.im)
        
        a = Complex(-3,-2)
        a = -a
        b = Complex(3,2)
        self.assertEqual(a.re,b.re)
        self.assertEqual(a.im,b.im)
        
    def test_invert(self):
        
        a = Complex(3,2)
        a = ~a
        b = Complex(3,-2)
        self.assertEqual(a.re,b.re)
        self.assertEqual(a.im,b.im)
        
        a = Complex(3,-2)
        a = ~a
        b = Complex(3,2)
        self.assertEqual(a.re,b.re)
        self.assertEqual(a.im,b.im)
        
    def test_roots(self):
        
        b = evaluate([1,2,3], roots([1,2,3]))
        
        if isinstance(b[0],(float,int)) and isinstance(b[1],(float,int)):
            self.assertEqual(b[0],0)
            self.assertEqual(b[1],0)
            
        elif isinstance(b[0],Complex) and isinstance(b[1],Complex):
            self.assertEqual(b[0].re,0)
            self.assertEqual(b[0].im,0)
            self.assertEqual(b[1].re,0)
            self.assertEqual(b[1].im,0)
            
        
if __name__ == '__main__':
    unittest.main()
    