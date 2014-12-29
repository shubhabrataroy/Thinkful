import pandas as pd
from os.path import join
log_path = "/home/sroy/Desktop/Thinkful"
df = pd.read_csv(join(log_path, 'LoanStats3b.csv'),low_memory=False)
df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

#df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)
# converts string to datetime object in pandas:
df['list_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('list_d_format') 
year_month_summary = dfts.groupby('issue_d').count()
loan_count_summary = year_month_summary['issue_d']
