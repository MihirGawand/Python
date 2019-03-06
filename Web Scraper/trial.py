# -*- coding: utf-8 -*-
"""
Created on Mon May 21 11:46:09 2018

@author: sgmih
"""

import urllib
import urllib.request
from bs4 import BeautifulSoup
import requests

def scrape_course(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html5lib')
    
#    coursedata = ""
    data = soup.find_all("table", {"cellspacing":"0"})
#    return data
    table = soup.find_all("tr", {"align":"center"})
    data = []
    for mytable in table:
        table_body = mytable.find_all('td')
        for td in table_body[0:7]:
            data.append(td.text.strip())

#    for r in table_heading:
#    return data
#    for r in table_heading:
#        r = r.text
#    return r
    
    data1 = data[0:7]
#    return data1
    
    Term = data1[0]
    CRN = data1[1]
    Instructor = data1[5]
    Days = data1[6]
    Days = Days[:-16]
    
    
    return Term, Days
    
    
#    for row in rows[1:]:
#        for data in row.findAll('td')[0:2]:
#            coursedata = coursedata + "," + data.text
#            print(coursedata)
    
#        uClient = uReq(url)
#        page_html = uClient.read()
#        uClient.close()
#        page_soup = soup(page_html, "html.parser")
#         response = requests.get(url)        
#         soup = BeautifulSoup(response.content, 'html5lib')
#         #contents = page_soup.find_all("tr",{"align":"center"})
#         table = soup.find_all("tr", {"align":"center"})
#          for mytable in table:
#               table_body = mytable.find_all('td')
#               for td in table_body:
#                   print(td.text.strip())
         
    
if __name__ == '__main__':
    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?Columns=afghijklmnopqrstuvwyz{&SubjectCode=ME&CourseNumber=451&Term=201901'
    
#    url = 'http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=' + area + '&coursenumber=' + str(coursenumber) + '&Term=' + str(term)
    a =  scrape_course(url)
    print(a)
    
    # bash command