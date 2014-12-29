import pandas as pd
import numpy as np 
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
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)  

##### Now the logistic part
intrate = loansData['Interest.Rate']
intrate[np.isnan(intrate)] = 0
loanamt = loansData['Amount.Requested']
loanamt[np.isnan(loanamt)] = 0
fico = loansData['FICO.Score']
fico[np.isnan(fico)] = 0
monthly_income = loansData['Monthly.Income']
monthly_income[np.isnan(monthly_income)] = 0
## It is not a value, so you need to convert it into we weigh them based on their importance
house_ownership = loansData['Home.Ownership']
house_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in house_ownership]

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x3 = np.matrix(monthly_income).transpose()
x4 = np.matrix(house_ownership).transpose()


x = np.column_stack([x1,x2,x3, x4])


X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
