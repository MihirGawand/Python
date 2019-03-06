# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:46:23 2018

@author: sgmih
"""

#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup



BASE_URL = "http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=ME&coursenumber=451"


def retrieve(url: str):

    r = requests.get(url, verify=False)
    soup = BeautifulSoup(r.text, "html5lib")
    return soup


def get_data():
    result_list = []
    new_result_list=[]

    def load_job_links_from(url):
        soup = retrieve(url)
        table=soup.find('table',attrs={'id':'ctl00_ContentPlaceHolder1_SOCListUC1_gvOfferings'})
        rows = (table.find_all(['td']))
        for i in rows:
            result_list.append(i.text.strip())

        chunks = [result_list[x:x + 22] for x in range(0, len(result_list),22)]

        for i in chunks:
            if i[0] == 'F18':
                list=[]
                list.append(i[0])
                list.append(i[1])
                list.append(i[5])
                list.append(i[6])

                new_result_list.append(list)

        return (new_result_list)


    return load_job_links_from(BASE_URL)


data = get_data()
print(data)