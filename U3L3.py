from bs4 import BeautifulSoup
import requests
import pandas as pd
#import numpy as np
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
column_name = ['country', 'year', 'total', 'men', 'women']
table = pd.DataFrame(records, columns = column_name )

con = lite.connect('/home/sroy/Desktop/Thinkful/Exercises/u3l4.db')
cur = con.cursor()

with con:
    cur.execute("DROP TABLE IF EXISTS gdp")
    cur.execute('CREATE TABLE gdp (country_name REAL, _1999 INT, _2000 INT, _2001 INT, _2002 INT, _2003 INT, _2004 INT, _2005 INT, _2006 INT, _2007 INT, _2008 INT, _2009 INT, _2010 INT);')

with open('/home/sroy/Desktop/Thinkful/Exercises/ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:-5]) + '");')

## combined frames
#df_combined = pd.merge(table,table_gdp_subset, how='inner', on='country')
