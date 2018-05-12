# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:40:16 2018

@author: sgmih
"""

#!/usr/bin/env python3

  #for row in rows:
      #  y = (row[91])
       # final_score.append(y)
    #print(final_score)
    
#import csv
#with open("grades.csv", "r") as csvfile:
#    csv_reader = csv.reader(csvfile)
#    next(csv_reader)
#    for row in csv_reader:
#        i = float(row[91])
#        print(i)
    

#import pandas
#import csv
#data = pandas.read_csv("grades.csv", converters={"Final Score":float})
#Score = data.Final_score.tolist()
#temp = sum(Score)
#print(temp)

#import csv
#with open('grades.csv') as csvfile:
#    spamreader = csv.reader(csvfile)
#    next(spamreader)
#    for row in spamreader:
#        sum = 0
#        for i in row[91]:
#            sum += float(i)
#    print(sum)

from pandas import DataFrame, read_csv
import csv
import numpy as np
from collections import defaultdict
import pandas as pd
with open('grades.csv') as f: #average
    reader = csv.DictReader(f)
    total = 0
    length = 0
    for row in reader:
        total += float(row['Final Score'])
        length = length + 1
    print(length)
    print(total)
    average = total/length
    print('the average is {}'.format(average))
    
with open('grades.csv') as csvfile: #AboveAverage
    reader = csv.DictReader(csvfile)
    above_average = 0
    for row in reader:
        if float(row['Final Score']) > average:
            above_average += 1
        else:
            pass
    print(above_average)
    
    
with open('grades.csv') as f: #median
    reader = csv.DictReader(f)
    a = 0
    finalscore = []
    for row in reader:
        a = float(row["Final Score"])
        finalscore.append(a)
    median = sorted(finalscore)[len(finalscore) // 2]
    print("median is {}".format(median))
    
with open('grades.csv') as grade:  #AboveMedian
    read = csv.DictReader(grade)
    above_median = 0
    for row in read:
        if float(row['Final Score']) > float(median):
            above_median += 1
        else:
            pass
    print(above_median)
        
with open('grades.csv') as f:
    read = csv.DictReader(f)
    Average_of_HW = []
    total = 0
    length = 0
    for row in read:
        try:
            total += float(row["Homework 1 (7083684)"])
            length += 1.0
        except ValueError:
            pass
    average = total/length
    Average_of_HW.append(average)
    print(Average_of_HW)

with open('grades.csv') as f:    
    read = csv.DictReader(f)
    x = [assign_name for assign_name in row.keys() if 'Homework' in assign_name and 'Score' not in assign_name and 'Practice' not in assign_name]
    print(x)
    i = 0
    for row in read:
        x = x[i]
        try:
            total += float(row[x])
            length += 1
        except ValueError:
            pass
        else:
            pass
            average = total/length
        i += 1
    Average_of_HW.append(average)
    print(Average_of_HW)
 

    

    
    
    
    
#    for row in csv.reader(f):
#        numbers = np.array([float(col) for col in row[91]])
#        numbersnz = numbers
#        if(numbersnz[1:]>average):
#            above_average += 1
#    print(above_average)
#            print(above_average)
#        else:
#            above_average = above_average + 0
#    print(above_average)
    

        
        
    
    
    
        
        
    
        
        
        
    
    
    
    
    
    