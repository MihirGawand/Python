# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:23:42 2018

@author: sgmih
"""

from pandas import DataFrame, read_csv
import csv
import numpy as np
from collections import defaultdict
import pandas as pd

def average_median(file):
    with open(file) as f:
        reader = csv.reader(f)
        data = list(reader)
        strength = float(len(data))
        
    with open(file) as f: #average
        reader = csv.DictReader(f)
        total = 0
        length = 0
        for row in reader:
            total += float(row['Final Score'])
            length = length + 1
        average = total/length
        print('Average Score:', average)
        
def hardest_assignment(file):
    df1 = pd.read_csv(file)
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
    for i in range(len(HW)):
        if HW[i] == Hardest_Assignment:
            print('Hardest Assignment:', 'Homework', i+1)
        else:
            pass
if __name__ == '__main__':
    file = 'grades.csv'
    average_median(file)
    hardest_assignment(file)