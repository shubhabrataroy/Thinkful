# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 20:15:19 2014

@author: shubhabrataroy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from itertools import islice, izip
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#def pairwise(t):
#    it = iter(t)
#    return izip(it, it)

A = loansData['FICO.Range'].tolist()
FICO = []
for j in range(len(A)):
    B = A[j].split("-")
    C = (int(B[0]),int(B[1]))
    C = np.mean(C)
    FICO.append(C)

loansData['FICO.Score'] = FICO
plt.figure()
p = loansData['FICO.Score'].hist()
plt.show()
