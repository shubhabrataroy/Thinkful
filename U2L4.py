import pandas as pd
#import numpy as np 
import statsmodels.api as sm

##### Same as before we did for linear regression

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#print the first 5 rows of each of the column to see what needs to be cleaned
print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
print loansData['FICO.Range'][0:5]

#cleaning up the columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

'''convert the data in FICO.Range into string and split the string and take the lowest value'''
loansData['FICO.Score'] = loansData['FICO.Range']
print loansData['FICO.Score'][0:5]
A =loansData['FICO.Score'].tolist()
FICO=[] #declare an empty array
for j in range(len(A)):   #for j in between 0 to len(A)
  B = A[j].split("-")     #split each sub-array on - and save it to B
  C = float(B[0])           #convert the string to int, using only the first value
  FICO.append(C)          #append each C to the empty array, using first value
loansData['FICO.Score']=FICO

##### Now the logistic part

intercept = [1] * len(loansData)
loansData['Intercept'] = intercept
# independant variables
ind_vars = ['Intercept', 'Amount.Requested', 'FICO.Score']
ir = loansData['Interest.Rate']
ir = [1 if x < 12 else 0 for x in ir]
loansData['IR_TF'] = ir
X = loansData[ind_vars]
y = loansData['IR_TF']
 
logit = sm.Logit(y, X)
result = logit.fit()
coeff = result.params
print coeff
