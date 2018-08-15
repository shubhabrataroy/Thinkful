#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:36:12 2018

@author: shubhabrataroy
"""

import seaborn as sns
import random

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")


def colors():
      r = random.random()
      g = random.random()
      b = random.random()
      return (r,g,b)


colors_ = [colors() if _y < 20 else (1, 0, 0) for _y in tips["total_bill"]]

ax = sns.barplot(x="day", y="total_bill", data=tips, palette=colors_)



 
