# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:12:16 2018

@author: sgmih
"""

#!/usr/bin/env python3

from pandas import DataFrame, read_csv
import csv
import numpy as np
from collections import defaultdict
import pandas as pd
from decimal import Decimal

def average_median(file):                                                      #This function answers the second question of the HW#1. 
    with open(file) as f:  
        reader = csv.reader(f)
        data = list(reader)
        strength = int(len(data)-1)                                            #to find the number of students in the class
        print(strength)             
        
    with open(file) as f: 
        reader = csv.DictReader(f)                                             #It uses the DictReader to access the column 'Final Score' and provides the required outputs
        total = 0
        length = 0
        for row in reader:
            try:
                total += float(row['Final Score'])
                length += 1
            except ValueError:
                pass
        average = total/length
        print('Average Score:', '{0:.2f}'.format(average))
    
    with open(file) as csvfile: #AboveAverage
        reader = csv.DictReader(csvfile)
        above_average = 0
        for row in reader:
            try:
                if float(row['Final Score']) > float(average):
                    above_average += 1
                else:
                    pass
            except ValueError:
                pass
        percent_above_avg = ((float(above_average)/float(strength))*100)
        print('Above Average:', '{0:.2f}'.format(percent_above_avg),'%')
    
    
    with open(file) as f: 
        reader = csv.DictReader(f)
        a = 0
        finalscore = []
        for row in reader:
            try:
                a = float(row["Final Score"])
                finalscore.append(a)
            except ValueError:
                pass
        median = sorted(finalscore)[strength // 2]
        print("Median Score", '{0:.2f}'.format(median))
    
    with open(file) as grade:  #AboveMedian
        read = csv.DictReader(grade)
        above_median = 0
        for row in read:
            try:
                if float(row['Final Score']) > float(median):
                    above_median += 1
                else:
                    pass
            except ValueError:
                pass
        percent_above_med = ((float(above_median)/float(strength))*100)
        print('Above Median:', '{0:.2f}'.format(percent_above_med), '%')

def hardest_assignment(file):                                                  #This function answers the third question of the HW#1
    df1 = pd.read_csv(file)
    cols = df1.columns.drop('Student Number')
    df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')                #convert the datatype to numeric, the errors statement considers exceptions such as 'EX' in this case 
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

def hardest_lab(file):                                                         #this function answers the fourth question 
    df1 = pd.read_csv(file)
    cols = df1.columns.drop('Student Number')
    df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
    Lab = []
    Lab.append((df1['Lab Quiz 1 (in Lab) on-campus students only (7083705)'].mean() + df1['Lab 1 Exercise (7083695)'].mean())/2) #calculate the mean of Lab Quizes and Lab Exercises
    Lab.append((df1['Lab Quiz 2 (7083706)'].mean() + df1['Lab 2 Exercise (7083696)'].mean())/2)
    Lab.append((df1['Lab Quiz 3 (7083707)'].mean() + df1['Lab 3 Exercise (7083697)'].mean())/2)
    Lab.append((df1['Lab Quiz 4 (7083708)'].mean() + df1['Lab 4 Exercise (7083698)'].mean())/2)
    Lab.append((df1['Lab Quiz 5 (7083709)'].mean() + df1['Lab 5 Exercise (7083699)'].mean())/2)
    Lab.append((df1['Lab Quiz 6 (7083710)'].mean() + df1['Lab 6 Exercise (7083700)'].mean())/2)
    Lab.append(df1['Lab Quiz 7 (7083711)'].mean() + df1['Lab 7 Exercise (7083701)'].mean()/2)
    Lab.append(df1['Lab Quiz 8 (7083712)'].mean() + df1['Lab 8 Exercise (7083702)'].mean()/2)
    Lab.append(df1['Lab Quiz 9 (7083713)'].mean() + df1['Lab 9 Exercise (7083703)'].mean()/2)
    Lab.append(df1['Lab Quiz 10 (7083704)'].mean() + df1['Lab 10 Exercise (7083694)'].mean()/2)
    Hardest_Lab = min(Lab)
    for i in range(len(Lab)):
        if Lab[i] == Hardest_Lab:
            print('Hardest Lab:', 'Lab', i+1)
        else:
            pass
        
def student_grades(file):                                                      #this function answers the fifth question 
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
    
def student_complain_grade(file):                                              #Question 6
    df = pd.read_csv(file)
    a = []                                                                      
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
    print(len(a),'students will complain about their grade')

def grade_cutoffs(file):                                                      #Question 6
    df = pd.read_csv(file)
    Final_score = df['Final Score']
    sort_Final_score = sorted(Final_score, key = float, reverse = True)        # Sort 'Final Score' in descending order
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

if __name__ == '__main__':
    file = 'grades.csv'                                                        #directs the variable to csv file to be accessed
    print('Question 2')
    average_median(file)
    print('Question 3')
    hardest_assignment(file)
    print('Question 4')
    hardest_lab(file)
    print('Question 5')
    student_grades(file)
    print('Question 6')
    student_complain_grade(file)
    print('Question 7')
    grade_cutoffs(file)
    
    
    
    
    