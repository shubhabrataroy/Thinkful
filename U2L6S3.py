# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 00:45:04 2015

@author: shubhabrataroy
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv('/Users/shubhabrataroy/Desktop/Thinkful/Data/LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

"""
Plot the loan data (loan_count_summary in from the previous assignment). Is the series stationary? 
If not, what would you do to transform it into a stationary series?
"""
plt.plot(loan_count_summary)

""" No it is not a stationary time series since it is increasing with time. We can differntiate it to
get another time series that might be stationary in nature. We test it in the following section """
loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)

plt.plot(loan_count_summary_diff)
""" we see some negative values here. So we add a threshold of 316 to all the terms (-316 being the minimum value) """
loan_count_summary_diff = loan_count_summary_diff + 316

"""  we can even smooth it out by diving with the maximum value """

loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)

plt.plot(loan_count_summary_diff)
""" However the series short enough to conclusively say that it is a stationary time series """

""" Plot out the ACF and PACF"""
sm.graphics.tsa.plot_acf(loan_count_summary_diff) # autocorrelation
sm.graphics.tsa.plot_pacf(loan_count_summary_diff) # partial autocorrelation
