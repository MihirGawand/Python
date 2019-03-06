# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:02:49 2018

@author: sgmih

Mihir Sunil Gawand: ME 599
"""

#!/usr/bin/env python3

import bs4

import urllib.request 
import re
from bs4 import BeautifulSoup

import requests

pattern = re.compile("^(.*\s\d+).\s+(([A-Z]+\s+)*).*$")

class Course():
    #Assigns the data returned from the course instance in the scrape_course function
    def __init__(self, subject1, subject2, term, coursenum, instructor, days, time):  
        self.subject1 = str(subject1)
        self.subject2 = str(subject2)
        self.term = term
        self.coursenum = coursenum
        self.instructor = instructor
        self.days = days
        self.time = time
        
    # Prints the data to provide the course details in an organized manner    
    def __str__(self):
        return self.subject1 + ': ' + self.subject2 + '\nTerm:{} '.format(self.term) + '\nCourse Number:{} '.format(self.coursenum) + '\nInstructor:{} '.format(self.instructor) + '\nDays:{} '.format(self.days) + '\nTime:{} '.format(self.time)
        

        
def scrape_course(department, coursenumber, term):
    
   #Inputs the variables in the URL to pull the specific URL for the given term
    if term == 'Sp18':
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(201803)
    elif term == 'Su18':
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(201900)
    elif term == 'F18':
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(201901)
    elif term == 'W19':
        url ='http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(201902)
    elif term == 'Sp19':
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(201903)
    elif term == 'Su19':
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber) + '&Term=' + str(202000)
    else:
        url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + str(department) + '&coursenumber=' + str(coursenumber)  
        
        
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html5lib')
    
    #Find the table that contains all the relevant course details
    table = soup.find_all("tr", {"align":"center"})
    data = []
       
    #finds the subject heading to get the name of the course
    subject = soup.find_all("h3")
    sub = subject[0].text.strip()
    sub = " ".join(sub.split())
#    print("sub = ", sub)
    textObj = pattern.match(sub)
    
    subject1 = textObj.group(1)
    subject2 = textObj.group(2)
    #subject = sub[:-4]
    
    # Used to extract only the details that are required from the table    
    for mytable in table:
        table_body = mytable.find_all('td')
        for td in table_body[0:7]:
            data.append(td.text.strip())
                
    data1 = data[0:7]
    
    # Assigns the details to the specific terms or values
    if len(data1) > 0:
        term = data1[0]
        coursenum = data1[1]
        instructor = data1[5]
        schedule = data1[6]
        days = schedule[0:3]
        time = schedule[3:12]
        return Course(subject1, subject2,
                      term, coursenum, instructor, days, time)
        
    # To consider exceptions i.e. if there is no table available
    else:
        return Course(subject1, subject2, None, None, None, None, None)
    
    
if __name__ == '__main__':

    #Test for ME 451 Winter 2019
    a = scrape_course('ME','451', 'W18')
    print(a)
    
    #URL to test if the code is returning correct values
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?Columns=afghijklmnopqrstuvwyz{&SubjectCode=ME&CourseNumber=451&Term=201902'
    
    #Below are the actual values from the webpage
    print('\nActual details of ME 451 Winter 2019')
    print('Term: W19')
    print('Course Number: 34839')
    print('Instructor: Smart, W.')
    print('Days: MW')
    print('Time: 0900-0950')
    

    #Test for ROB 514 Fall 18
    b = scrape_course('ROB','514','W18')
    print('\n',b)
    
    #URL to check if the code is returning the correct values
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?Columns=afghijklmnopqrstuvwyz{&SubjectCode=ROB&CourseNumber=514&Term=201901'
    
    
    
    #Test for other subject
    c = scrape_course('CS','515','F18')
    print('\n',c)
    
    #URL to test if the code is returing correct values
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?Columns=afghijklmnopqrstuvwyz{&SubjectCode=CS&CourseNumber=515&Term=201901'
    
    #Test values from webpage for CS 519 Fall term course
    print('\nActual details of CS 517 Summer 2018:')
    print('CS 515: ALGORITHMS AND DATA STRUCTURES')
    print('Term: F18')
    print('Course Number: 10413')
    print('Instructor: Borradaile, G.')
    print('Days: TR')
    print('Time: 1800-1920')
    
    
    
    
    
    
    
    
    