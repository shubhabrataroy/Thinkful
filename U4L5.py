# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 15:46:25 2015

@author: sroy
"""
import pandas as pd
import numpy as np
from scipy.cluster.vq import kmeans, vq,  whiten
from pylab import plot,show

# can use this one for calculating Euclidian distance
def Wk(mu, clusters):
    K = len(mu)
    return sum([np.linalg.norm(mu[i]-c)**2/(2*len(c)) \
               for i in range(K) for c in clusters[i]])

un_data = pd.read_csv('/home/sroy/Desktop/Thinkful/un.csv')
# number of rows and columns
un_data.shape

#returns the total number of non-null values within each column
un_data.count()

"""country and region have the maximum non-null values. We should cluster on these two columns."""
list_of_countries = list(set(un_data['country']))
no_of_country = len(list_of_countries)


#extracting the required columns
lifemale = un_data['lifeMale']
gdp = un_data['GDPperCapita']
lifefemale = un_data['lifeFemale']
infantmortality = un_data['infantMortality']

#replacing the NaN with 0
lifemale[np.isnan(lifemale)]  = 0
gdp[np.isnan(gdp)] = 0
lifefemale[np.isnan(lifefemale)] = 0
infantmortality[np.isnan(infantmortality)] = 0

# You have to create a matrix where there are two columns and 207 rows, which was not the case in your code
d1 = {'gdp': gdp, 'lifemale': lifemale}
df1 = pd.DataFrame(d1)
cluster1 = df1.values
 # must be called prior to passing an observation matrix to kmeans. Normalize a group of observations on a per feature basis.
cluster1 = whiten(cluster1)
centroids1,dist1 = kmeans(cluster1,2)
idx1,idxdist1 = vq(cluster1,centroids1)

plot(cluster1[idx1==0,0],cluster1[idx1==0,1],'ob',
     cluster1[idx1==1,0],cluster1[idx1==1,1],'or')
plot(centroids1[:,0],centroids1[:,1],'sg',markersize=8)
show()

## check all clusters:
cluster1 = whiten(cluster1)
average_distance = []
for k in range(1,11):
    centroids1,dist1 = kmeans(cluster1,k) # you can calculate the eucledean distance in the next line
    idx1,idxdist1 = vq(cluster1,centroids1)
    avg_dist = np.mean(idxdist1)
    average_distance.append(avg_dist)
# Just plotting the mean distance, you can plot Euclidian distance once you update the code
plot(range(1,11), average_distance)
