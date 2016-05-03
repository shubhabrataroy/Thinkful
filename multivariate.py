import pandas as pd
import numpy as np 
import statsmodels.formula.api as smf
from patsy.contrasts import Treatment

##### Same as before we did for linear regression

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#cleaning up the columns
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: x.rstrip('%'))
loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: x.rstrip('months'))

'''convert the data in FICO.Range into string and split the string and take the lowest value'''

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: (x.split('-')))
loansData['FICO.Score'] = loansData['FICO.Score'].map(lambda x: int(min(x)))

loansData['Interest.Rate'] = loansData['Interest.Rate'].astype(float)  

##### Now the logistic part
intrate = loansData['Interest.Rate']
intrate[np.isnan(intrate)] = 0
loanamt = loansData['Amount.Requested']
loanamt[np.isnan(loanamt)] = 0
fico = loansData['FICO.Score']
fico[np.isnan(fico)] = 0
loansData['log_income'] = np.log1p(loansData['Monthly.Income'])

ownership_dummies = pd.get_dummies(loansData['Home.Ownership'], prefix='ownership').iloc[:, 1:]

# concatenate the dummy variable colums onto the original DataFrame (axis)
data = pd.concat([loansData, ownership_dummies], axis=1)
data.rename(columns={'Interest.Rate': 'Interest_Rate'}, inplace=True) # just getting rid of some stupid errors

est = smf.ols(formula="Interest_Rate ~ log_income + ownership_NONE + ownership_OTHER +ownership_OWN + ownership_RENT", data=data).fit()

est.summary()

#################################################################

loansData_ = loansData
levels = ['NONE', 'OTHER', 'RENT', 'OWN', 'MORTGAGE']
ownership_dummies1 = Treatment(reference=0).code_without_intercept(levels)

#ownership_dummies1.matrix[loansData_.house_ownership-1, :]
loansData_.rename(columns={'Interest.Rate': 'Interest_Rate'}, inplace=True)
mod = smf.ols("Interest_Rate ~ C(log_income, Treatment)", data=loansData_).fit()

mod.summary()
