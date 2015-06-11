
# New Yorkers Bike
import time
import requests
from dateutil.parser import parse
import collections
import sqlite3 as lite
import pandas as pd
import matplotlib.pyplot as plt
import collections

con = lite.connect('SQLite Data\citi_bike.sqlite')
cur = con.cursor()

for i in range(60):
    r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time = parse(r.json()['executionTime'])

    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%c'),))
    con.commit()
    
    id_bikes = collections.defaultdict(int)
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = '" + exec_time.strftime('%c') + "';")
    con.commit()

    time.sleep(60)
con.close()

### Analysis

con = lite.connect('SQLite Data\citi_bike.sqlite')
cur = con.cursor()

hour_data = pd.read_sql_query("SELECT * FROM available_bikes WHERE execution_time like '06/07/15%' ORDER BY execution_time",con,index_col='execution_time')
hour_change = collections.defaultdict(int)
for col in hour_data.columns:
    station_vals = hour_data[col].tolist()
    station_id = col[1:] #trim the "_"
    station_change = 0
    for k,v in enumerate(station_vals):
        if k < len(station_vals) - 1:
            station_change += abs(station_vals[k] - station_vals[k+1])
    hour_change[int(station_id)] = station_change

def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

max_station = keywithmaxval(hour_change)
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data_max_station = cur.fetchone()
con.close()
print "The most active station is station id %s at %s latitude: %s longitude: %s " % data_max_station
print "With " + str(hour_change[max_station]) + " bicycles coming and going in the hour between " + str(hour_data.index[0]) + " and " + str(hour_data.index[-1])
plt.bar(hour_change.keys(), hour_change.values())
plt.show()
