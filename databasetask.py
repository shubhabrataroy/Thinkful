# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:41:41 2014

@author: sroy
"""

import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql
import sys

""" Connect to the database """
con = lite.connect('/home/sroy/ThinkfulTest1.db')
cur = con.cursor()

# readlink -f foo.bar
#cur = con.cursor()    
#cur.execute('SELECT SQLITE_VERSION()')
#data = cur.fetchone()

#with con:
#  # From the connection, you get a cursor object. The cursor is what goes over the records that result from a query.
#  cur = con.cursor()    
#  cur.execute('SELECT SQLITE_VERSION()')
#  # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
#  data = cur.fetchone()
#  # Finally, print the result.
#  print "SQLite version: %s" % data
#
## Inserting rows by passing values directly to `execute()`
#with con:
#
#    cur = con.cursor()
#    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
#    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
#
#with con:
#    cur = con.cursor()    
#    cur.execute("SELECT * FROM cities")
#    rows = cur.fetchall()
""" Create the cities and weather tables """
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")

""" Insert data into the two tables """
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text)")
cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January')")
cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January')")


""" Load into pandas data-frame"""
query_cities = "select * from cities"
cities = pd.read_sql(query_cities,con)
# or cities = psql.frame_query(query_cities,con)

query_weather = "select * from weather"
weather = pd.read_sql(query_weather,con)
weather["name"] = weather["city"]
weather.drop('city', axis=1, inplace=True)

""" join two data frames """
combined = pd.DataFrame.merge(cities,weather, how='inner', left_on = 'name', right_on = 'name')
together = combined.apply(lambda x:'%s, %s' % (x['name'],x['state']),axis=1)

""" Print out the resulting city and state in a full sentence. For example The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA """
print "cities that are warmest in July are:", ', '.join(together.tolist())

""" Dynamic input to a query """
year = 2013
query_weather_dynamic = " SELECT * FROM weather WHERE year = " + str(int(year))
weather_dynamic = psql.frame_query(query_weather_dynamic,con)
