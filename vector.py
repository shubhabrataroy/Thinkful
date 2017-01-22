# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:22:57 2017

@author: shubhabrataroy
"""

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, b):
        return Vector(self.x + b.x, self.y + b.y)
        
    
