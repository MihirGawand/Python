# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:18:18 2018
    
@author: sgmih
"""
from pandas import DataFrame, read_csv
import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
import numpy as np


file = r'grades.csv'
df = pd.read_csv(file)
df.replace('EX', np.NaN)
print(df['Final Score'])
S = df['Final Score'].mean()
print(S)

df1 = pd.read_csv(file)
#df1['Homework 1 (7083684)'] = pd.to_numeric(df1['Homework 1 (7083684)'], errors = 'coerce')

cols = df1.columns.drop('Student Number')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
HW = []
HW.append(df1['Homework 1 (7083684)'].mean())
HW.append(df1['Homework 2 (7083685)'].mean())
HW.append(df1['Homework 3 (7083686)'].mean())
HW.append(df1['Homework 4 (7083687)'].mean())
HW.append(df1['Homework 5 (7083688)'].mean())
HW.append(df1['Homework 6 (7083689)'].mean())
HW.append(df1['Homework 7 (7083690)'].mean())
HW.append(df1['Homework 8 (7083691)'].mean())
HW.append(df1['Homework 9 (7083692)'].mean())
Hardest_Assignment = min(HW)
print('Hardest Assignment:', Hardest_Assignment)

Lab = []
Lab.append(df1['Lab Quiz 1 (in Lab) on-campus students only (7083705)'].mean())
Lab.append(df1['Lab Quiz 2 (7083706)'].mean())
Lab.append(df1['Lab Quiz 3 (7083707)'].mean())
Lab.append(df1['Lab Quiz 3 (7083707)'].mean())
Lab.append(df1['Lab Quiz 4 (7083708)'].mean())
Lab.append(df1['Lab Quiz 5 (7083709)'].mean())
Lab.append(df1['Lab Quiz 6 (7083710)'].mean())
Lab.append(df1['Lab Quiz 7 (7083711)'].mean())
Lab.append(df1['Lab Quiz 8 (7083712)'].mean())
Lab.append(df1['Lab Quiz 9 (7083713)'].mean())
Hardest_Lab = min(Lab)
print('Hardest Lab:', Hardest_Lab)










#df['Homework 1 (7083684)'].replace('EX',np.NaN)
#HW = df['Homework 1 (7083684)'].mean()
#print(HW)
#HW2 = df['Homework 2 (7083685)'].mean()
#HW3 = df['Homework 3 (7083686)'].mean()
#HW4 = df['Homework 4 (7083687)'].mean()
#HW5 = df['Homework 5 (7083688)'].mean()
#HW6 = df['Homework 6 (7083689)'].mean()
#HW7 = df['Homework 7 (7083690)'].mean()
#HW8 = df['Homework 8 (7083691)'].mean()
#HW9 = df['Homework 9 (7083692)'].mean()
#print(HW1)

#HW_averages = [HW1, HW2, HW3, HW4, HW5, HW6, HW7, HW8, HW9]