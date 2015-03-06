import sqlite3 as lite
import pandas as pd
from geopy.geocoders import Nominatim

con = lite.connect('C:\sqlite\Baltimore_crime_study.db')

query_speed_camera = "SELECT * FROM Speed_Camera" 
SC = pd.read_sql(query_speed_camera,con)

SC['intersection'] = SC['street'] + " " + SC['crossStreet']
geolocator = Nominatim()
x = geolocator.reverse("39.2364856246, -76.6122106478")
#y = geolocator.reverse(coord[1])
location = []
for j in SC['Location 1']:
    k = j.replace('(','')
    k = k.replace(')', '')
    add = geolocator.reverse(k)
    location.append(add.address)

SC['location'] = location

#####################################################################################

import pandas as pd
CS = pd.io.excel.read_excel('/Users/shubhabrataroy/Desktop/Thinkful/Data/CrimeStatistics.xlt', sheetname=0)

def getSec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
seconds = []
for i in range(len(CS)):
    if ((':' in str(CS['CrimeTime'][i])) == True):
        s = getSec(str(CS['CrimeTime'][i]))
    else:
        s = CS['CrimeTime'][i]
    seconds.append(s)
CS['CrimeTimeinSeconds'] = seconds

