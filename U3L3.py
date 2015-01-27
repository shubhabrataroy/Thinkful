# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:23:41 2015

@author: shubhabrataroy
"""
from bs4 import BeautifulSoup
import requests
import re

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)
soup = BeautifulSoup(r.content)
for row in soup('table'):
    print row
    
for tag in soup.find_all(re.compile("^t")): # find all tag start with t
    print tag.name
    
