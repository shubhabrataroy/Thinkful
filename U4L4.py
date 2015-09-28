# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:26:06 2015

@author: sroy
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_df = pd.DataFrame()
iris_df['sepal_length'] = iris.data[:,0]
iris_df['sepal_width'] = iris.data[:,1]
iris_df['petal_length'] = iris.data[:,2]
iris_df['petal_width'] = iris.data[:,3]
iris_df['target'] = iris.target
iris_df['target_flower'] = iris.target
iris_df['target_flower'].replace(0, 'setosa', inplace = True)
iris_df['target_flower'].replace(1, 'versicolor', inplace = True)
iris_df['target_flower'].replace(2, 'virginica', inplace = True)

neigh = KNeighborsClassifier()
X = [[x] for x in iris_df['sepal_length'].tolist()]
y = iris_df['sepal_width'].tolist()
neigh.fit(X, y)

test_y = 2.7645599698683703
test_x = 6.031175522438984

print neigh.predict([[test_y], [test_x]])
