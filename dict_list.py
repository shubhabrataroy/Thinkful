# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 20:54:02 2015

@author: shubhabrataroy
"""

""" 
Difference between a list and a dictionaryL

A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").

When you have to take one value and "look up" another value. In fact you could call dictionaries "look up tables."

Use a list for any sequence of things that need to be in order, and you only need to look them up by a numeric index.
"""


""" create a dictionary whose values are lists """

from collections import defaultdict
d = defaultdict(list)
a = ['1', '2']
for i in a:
    for j in range(int(i), int(i) + 2):
        d[j].append(i)

print d

""" or """
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in s:
        d[k].append(v)

d.items()

        
