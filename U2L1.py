import pandas as pd
from scipy import stats #need this to calculate mode

data = '''Region,Alcohol,Tobacco

North,6.47,4.03

Yorkshire,6.13,3.76

Northeast,6.19,3.77

East Midlands,4.89,3.34

West Midlands,5.63,3.47

East Anglia,4.52,2.92

Southeast,5.89,3.20

Southwest,4.79,2.71

Wales,5.27,3.53

Scotland,6.08,4.51

Northern Ireland,4.02,4.56''' 

#split the string on the hidden characters that indicate newlines
data = data.splitlines()
#print data

#split each iten in this list on the commas
data = [i.split(',') for i in data]
#print data

#create pandas dataframe
column_names = list(data[0]) #first row
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = column_names)

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#convert columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#calculate mean
alc_mean = df['Alcohol'].mean()
tob_mean = df['Tobacco'].mean()
print "The mean of the alcohol and tobacco is %.2f %.2f" %(alc_mean, tob_mean)

#calculate median
alc_median = df['Alcohol'].median()
tob_median = df['Tobacco'].median()
print "The median of the alcohol and tobacco is %.2f %.2f" %(alc_median, tob_median)

#calculate mode
alc_mode = stats.mode(df['Alcohol'])
tob_mode = stats.mode(df['Tobacco'])
print "The mode of the alcohol and tobacco is %.2f %.2f" %(float(alc_mode[0]), float(tob_mode[0]))
