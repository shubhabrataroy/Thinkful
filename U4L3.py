# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:30:54 2015

@author: sroy
"""

import pandas as pd
from os.path import join
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

saved_data_path = '/home/sroy/Desktop/Thinkful/'
df  = pd.read_csv(join(saved_data_path,'ideal_weight.csv'), names=['id', 'sex', 'actual', 'ideal', 'diff'], header=0)
df['sex'] = df['sex'].map(lambda x: x.replace("'",""))


plt.figure()
plt.hist([df['actual'], df['ideal']], histtype='bar', stacked=False)
plt.show()

# Convert into categorical variable
df['gender'] = pd.Categorical(df['sex'].tolist())


gnb = GaussianNB()
data = df[['actual','ideal','diff']]
target = df['gender']
model = gnb.fit(data, target)
y_pred = model.predict(data)
print("Number of mislabeled points out of a total %d points: %d" %(data.shape[0], (target != y_pred).sum()))

# Predict the sex for an actual weight of 145, an ideal weight of 160, and a diff of -15." 

d = {'actual': 145, 'ideal': 160, 'diff': -15}
df = pd.DataFrame(data=d, index=[1])
df = df[['actual','ideal', 'diff']]
pred = model.predict(df)
print pred
