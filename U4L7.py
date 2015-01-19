# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 17:08:38 2015

@author: sroy
"""
from sklearn import decomposition
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)

neigh = KNeighborsClassifier(n_neighbors=6)
neigh.fit(X,y).predict(X)
