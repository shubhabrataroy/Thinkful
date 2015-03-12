import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

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
for j in range(len(A)):   
  B = A[j].split("-")    
  C = float(B[0])           
  FICO.append(C)        
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

def logistic_function(FicoScore, LoanAmount,coeff):
    """ p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount)) """
    prob = 1/(1+exp(coeff[0]+coeff[2]*FicoScore+coeff[1]*LoanAmount))
    if prob > 0.7:
        p = 1
    else:
        p = 0
    return prob, p
    
prob = logistic_function(720, 10000,coeff)[0]
decision = logistic_function(720, 10000,coeff)[1]
    
## plotting: lets test different FICO score for 10,000 USD loan
Fico = range(550, 950, 10)
p_plus = []
p_minus = []
p = []
for j in Fico:
    p_plus.append(1/(1+exp(coeff[0]+coeff[2]*j+coeff[1]*10000)))
    p_minus.append(1/(1+exp(-coeff[0]-coeff[2]*j-coeff[1]*10000)))
    p.append(logistic_function(j, 10000,coeff)[1])

plt.plot(Fico, p_plus, label = 'p(x) = 1/(1+exp(b+mx))', color = 'blue')
plt.hold(True)
plt.plot(Fico, p_minus, label = 'p(x) = 1/(1+exp(-b-mx))', color = 'green')    
plt.hold(True)
plt.plot(Fico, p, 'ro', label = 'Decision for 10000 USD')
plt.legend(loc='upper right')
plt.xlabel('Fico Score')
plt.ylabel('Probability and decision, yes = 1, no = 0')
