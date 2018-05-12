# -*- coding: utf-8 -*-
"""
Created on Tue May  1 14:49:12 2018

@author: sgmih
"""

#!/usr/bin/env python3

from pandas import DataFrame, read_csv
import pandas as pd
import numpy as np

file = r'grades.csv'
df = pd.read_csv(file)
A = []
A1 = []
B1 = []
B2 = []
B3 = []
C1 = []
C2 = []
C3 = []
D1 = []
D2 = []
D3 = []
F = []
a = 0

for i in df.values:
    x=(i[len(i)-1])
    if x > int(94):
        A.append(x)
    else:
        if x > int(90) and x < int(94):
            A1.append(x)
        else:
            if x > int(87) and x < int(90):
                B1.append(x)
            else:
                if x > int(84) and x < int(87):
                    B2.append(x)
                else:
                    if x > int(80) and x < int(84):
                        B3.append(x)
                    else:
                        if x > int(77) and x < int(80):
                            C1.append(x)
                        else:
                            if x > int(74) and x < int(77):
                                C2.append(x)
                            else:
                                if x > int(70) and x < int(74):
                                    C3.append(x)
                                else:
                                    if x > int(67) and x < int(70):
                                        D1.append(x)
                                    else:
                                        if x > int(64) and x < int(67):
                                            D2.append(x)
                                        else:
                                            if x > int(61) and x < int(64):
                                                D3.append(x)
                                            else:
                                                if x > int(0) and x < int(61):
                                                    F.append(x)     
        
print('A',len(A))
print('A-',len(A1))  
print('B+',len(B1))
print('B',len(B2))
print('B-',len(B3))
print('C+',len(C1))
print('C',len(C2))
print('C-',len(C3))
print('D+',len(D1))
print('D',len(D2))
print('D-',len(D3))
print('F',len(F))
             


    
    


