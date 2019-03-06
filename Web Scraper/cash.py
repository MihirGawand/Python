#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ME 499/599 Spring 2018

Dollars class example
"""

import requests
from bs4 import BeautifulSoup


class Dollars:
    rates = None
    
    def __init__(self, dollars=0, cents=0):
        self.pennies = int(dollars * 100) + int(cents)
    
        # Get today's exchange rates, if we don't already have them
        if Dollars.rates == None:         
            Dollars.get_forex_rates()
        
    def __str__(self):
        return '{0}${1}.{2:02}'.format('-' if self.pennies < 0 else '',
            int(abs(self.pennies / 100)), abs(self.pennies) % 100)
        
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        try:
            return Dollars(cents=self.pennies + other.pennies)
        except:
            return self + Dollars(other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other - self
    
    def __neg__(self):
        return Dollars(cents=-self.pennies)
    
    def __mul__(self, other):
        return Dollars(cents=self.pennies * other)
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        return Dollars(cents=self.pennies / other)
    
    def __lt__(self, other):
        try:
            return self.pennies < other.pennies
        except:
            return self.pennies < Dollars(other)

    def get_forex_rates():
        response = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
        soup = BeautifulSoup(response.text, 'html5lib')

        Dollars.rates = {'EUR': 1.0}
        for item in soup.find_all('cube'):        
            try:
                Dollars.rates[item.get('currency')] = float(item.get('rate'))
            except:
                pass
        
        # Convert these to be multiples of dollars
        conversion = Dollars.rates['USD']
        for k,v in Dollars.rates.items():
            Dollars.rates[k] /= conversion
        
    def convert(self, currency):
        return Dollars.rates[currency] * self.pennies / 100

               
if __name__ == '__main__':
    a = Dollars()
    b = Dollars(1)
    c = Dollars(1.2334)
    d = Dollars(2, 6)
    e = Dollars(11878)
    
    a = b * 2
    print(a)
    a = a / 2
    print(a)
    
#    print()
#    print(c, d, c - d)

    print('{0} is EUR {1}'.format(e, e.convert('EUR')))
    
# Difference between class variable and instance variable
# self.get_forex_rates() doesn't work, but Dollars.get_forex_rates() does
# Notice the lack of self in the function definition
# Show that we only get rates once
# Could trigger download in convert function.  Or in external function on load.
    