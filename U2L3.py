import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print the first 5 rows of each of the column to see what needs to be cleaned
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

#cleaning up the columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))
#loansData[‘FICO.Score’] = [str(x) for x in loansData[‘FICO.Range’]] # another way
#loansData[‘FICO.Score’]   =    loansData[‘FICO.Score’].map(lambda x: x[:3])

#printing again to see if cleaning took place or not
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]

'''convert the data in FICO.Range into string and split the string and take the lowest value'''
loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()
#print (A)
FICO=[] #declare an empty array
for j in range(len(A)):   #for j in between 0 to len(A)
  B = A[j].split("-")     #split each sub-array on - and save it to B
  #C = int(B[0], B[1])    #convert the str to int
  #C = np.mean(C)         #finding the mean of B[0] and B[1]
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
loansData['FICO.Score']=FICO

#plot histogram
plt.figure()
p=loansData['FICO.Score'].hist()
plt.show()

#create a scatterplot matrix
a=pd.scatter_matrix(loansData, alpha=0.05, figure=(10,10))
plt.show()

#plots on the diagonal showing histogram for each variable. 
a=pd.scatter_matrix(loansData, alpha=0.05, figure=(10,10), diagonal='hist')
plt.show()

#regression analysis of the cleaned up columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
intrate = loansData['Interest.Rate']
intrate = [int(x) for x in intrate]
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

#the columns are returned as Series, so reshape required.
#the matrix transpose takes the column and return them as 1d-array 
y = np.matrix(intrate).transpose()  #dependent variable
print (y)
x1 = np.matrix(fico).transpose()    #independent variable
x2 = np.matrix(loanamt).transpose() #independent variable
print(x1)
print(x2)

#take the independent matrix and create an input matrix, 1 col for each variable
x = np.column_stack([x1,x2])

#creating the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
