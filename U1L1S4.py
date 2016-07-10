# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:40:08 2015

@author: sroy
"""

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for j in actors.keys():
    print j, 'played the role of', actors[j]
    
##################################################################
####  To preserve the order:
##################################################################
from collections import OrderedDict
actors=OrderedDict()
actors['Kyle MacLachlan']='Dale Cooper'
actors['Sheryl Lee']='Laura Palmer'
actors['Lara Flynn Boyle']='Donna Hayward'
actors['Sherilyn Fenn']='Audrey Horne'
    
for j in actors.keys():
    print j, 'played the role of', actors[j]
    
##################################################################
    
covered_A = 0
covered_B = 0

while (covered_A+covered_B < 102):
    covered_A += 2
    covered_B += 1
print (covered_A, covered_B)    

###################################################################

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

x = 'Jamie Theakston'
#x = "Sarah Hughes"
try:
    print phone_book[x]
except KeyError:
    print "Invalid Name"
        
