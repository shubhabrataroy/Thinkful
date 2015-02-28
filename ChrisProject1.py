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

