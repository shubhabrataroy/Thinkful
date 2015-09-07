from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3 as lite
import csv

url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)
soup = BeautifulSoup(r.content)
A = soup('table')[6].findAll('tr', {'class': 'tcont'})
B = [x for x in A if len(x)== 25] # removing records without value

records = []
for rows in B:
    col = rows.findAll('td')
    country = col[0].string
    year = col[1].string
    total = col[4].string
    men = col[7].string
    women = col[10].string
    record = (country, year, total, men, women)
    records.append(record)
column_name = ['country', 'year', 'total_schoollife', 'men_schoollife', 'women_schoollife']
table_schoollife = pd.DataFrame(records, columns = column_name )
table_schoollife=table_schoollife.dropna(axis=1,how='all')

con = lite.connect('/home/sroy/Desktop/Thinkful/Exercises/u3l4.db')
cur = con.cursor()

with con:
    cur.execute("DROP TABLE IF EXISTS gdp")
    cur.execute('CREATE TABLE gdp (country REAL, GDP_1999 INT, GDP_2000 INT, GDP_2001 INT, GDP_2002 INT, GDP_2003 INT, GDP_2004 INT, GDP_2005 INT, GDP_2006 INT, GDP_2007 INT, GDP_2008 INT, GDP_2009 INT, GDP_2010 INT);')

with open('/home/sroy/Desktop/Thinkful/Exercises/ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country, GDP_1999, GDP_2000, GDP_2001, GDP_2002, GDP_2003, GDP_2004, GDP_2005, GDP_2006, GDP_2007, GDP_2008, GDP_2009, GDP_2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:-5]) + '");')

# 
sql_statement = 'select * from gdp'
table_gdp = pd.read_sql(sql_statement, con)
table_gdp=table_gdp.dropna(axis=1,how='all')
## common countries
list1 = list(set(table_schoollife['country'].tolist()))
list2 = list(set(table_gdp['country'].tolist()))
list_common_countries = list(set(list1) & set(list2))

gdp = []
school_life_T = []
school_life_M = []
school_life_W = []
for j in list_common_countries:
    df1 = table_schoollife[table_schoollife['country']==j]
    df2 = table_gdp[table_gdp['country']==j]
    if (df2['GDP_'+ df1['year'].irow(0)].irow(0) != ''):
        school_life_T.append(int(df1['total_schoollife'].irow(0)))
        school_life_M.append(int(df1['men_schoollife'].irow(0)))
        school_life_W.append(int(df1['women_schoollife'].irow(0)))
        gdp.append(np.log(df2['GDP_'+ df1['year'].irow(0)].irow(0)))
    
df_final = pd.DataFrame({'Total': school_life_T, 'Men':school_life_M, 'Women': school_life_W, 'gdp': gdp})    
    
print df_final.corr()

