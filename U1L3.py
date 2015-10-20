# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 11:41:41 2014

@author: sroy
"""

import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql

""" Connect to the database """
con = lite.connect('/home/sroy/ThinkfulTest1.db')
cur = con.cursor()

populate_cities = """
INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');
"""
populate_weather = """
INSERT INTO weather (city,year,warm_month,cold_month,average_high) VALUES
    ('New York City',2013,'July','January',62),
    ('Boston',2013,'July','January',59),
    ('Chicago',2013,'July','January',59),
    ('Miami',2013,'August','January',84),
    ('Dallas',2013,'July','January',77),
    ('Seattle',2013,'July','January',61),
    ('Portland',2013,'July','December',63),
    ('San Francisco',2013,'September','December',64),
    ('Los Angeles',2013,'September','December',75);
"""


""" Create the cities and weather tables """
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("CREATE TABLE weather (city text,year integer,warm_month text,cold_month text,average_high integer)")

""" Populate the tables """
cur.execute(populate_weather)
cur.execute(populate_cities)

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

""" pick the records where July is the warmest month """
combined_july = combined[combined['warm_month'] == 'July']

""" Print out the resulting city and state in a full sentence. For example The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA """
together = combined_july.apply(lambda x:'%s, %s' % (x['name'],x['state']),axis=1)
print "cities that are warmest in July are:", ', '.join(together.tolist())

""" Dynamic input to a query """
year = 2013
query_weather_dynamic = " SELECT * FROM weather WHERE year = " + str(int(year))
weather_dynamic = psql.frame_query(query_weather_dynamic,con)


############################
z = zip(combined_july['name'], combined_july['state'])

for j in range(len(z)):
    print 'Number', (j+1), 'city having warmest month in July is', z[j][0], z[j][1]
