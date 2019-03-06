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
A = []          #Question 5
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

for i in df.values:
    x=(i[len(i)-1])
    if x >= int(94):
        A.append(x)
    else:
        if x >= int(90) and x < int(94):
            A1.append(x)
        else:
            if x >= int(87) and x < int(90):
                B1.append(x)
            else:
                if x >= int(84) and x < int(87):
                    B2.append(x)
                else:
                    if x >= int(80) and x < int(84):
                        B3.append(x)
                    else:
                        if x >= int(77) and x < int(80):
                            C1.append(x)
                        else:
                            if x >= int(74) and x < int(77):
                                C2.append(x)
                            else:
                                if x >= int(70) and x < int(74):
                                    C3.append(x)
                                else:
                                    if x >= int(67) and x < int(70):
                                        D1.append(x)
                                    else:
                                        if x >= int(64) and x < int(67):
                                            D2.append(x)
                                        else:
                                            if x >= int(61) and x < int(64):
                                                D3.append(x)
                                            else:
                                                if x >= int(0) and x < int(61):
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

a = []                      #Question 6
for i in df.values:
    x=(i[len(i)-1])
    if x >= float(93.5) and x < int(94): 
        a.append(x)
    else:
        if x >= float(89.5) and x < int(90):
            a.append(x)
        else:
            if x >= float(86.5) and x < int(87):
                a.append(x)
            else:
                if x >= float(83.5) and x < int(84):
                    a.append(x)
                else:
                    if x >= float(79.5) and x < int(80):
                        a.append(x)
                    else:
                        if x >= float(76.5) and x < int(77):
                            a.append(x)
                        else:
                            if x >= float(73.5) and x < int(74):
                                a.append(x)
                            else:
                                if x >= float(69.5) and x < int(70):
                                    a.append(x)
                                else:
                                    if x >= float(66.5) and x < int(67):
                                        a.append(x)
                                    else:
                                        if x >= float(63.5) and x < int(64):
                                            a.append(x)
                                        else:
                                            if x >= float(60.5) and x < int(61):
                                                a.append(x)
                                            else:
                                                pass                                          
print(a)
print(len(a),'students will complain about their grade')

print(len(df['Final Score']))             #Question 7

mean = df['Final Score'].mean()
std_dev = df['Final Score'].std()

print(mean)
print(std_dev)

#result = df.sort_values(['Final Score'], ascending = True)
#print(result)

#sort = []
#for i in result:
#    x=(i[len(i)-1])
#    print(x)
#    sort.append(x)

Final_score = df['Final Score']
sort_Final_score = sorted(Final_score, key = float, reverse = True)
A = int(0.1*(len(sort_Final_score)))
B = int(0.2*(len(sort_Final_score)))
C = int(0.3*(len(sort_Final_score)))
D = int(0.3*(len(sort_Final_score)))
F = len(sort_Final_score) - A - B - C - D

gradeA = sort_Final_score[:A]
gradeB = sort_Final_score[A:A+B]
gradeC = sort_Final_score[A+B:A+B+C]
gradeD = sort_Final_score[A+B+C:A+B+C+D]
gradeF = sort_Final_score[A+B+C+D:A+B+C+D+F]

print('A',min(gradeA))
print('B',min(gradeB))
print('C', min(gradeC))
print('D', min(gradeD))
print('F', min(gradeF))
    
    
    
#or () or () or () or () or () or () or () or (]:
    
    


