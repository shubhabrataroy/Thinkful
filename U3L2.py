import requests
#from pandas.io.json import json_normalize
#import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import datetime
#import time
#import json

# a package for parsing a string into a Python datetime object
#from dateutil.parser import parse 

#import collections

API_KEY = "96a47b0d63b4f8bd4bc1006f4c9bd789"

# sample URL https://api.forecast.io/forecast/96a47b0d63b4f8bd4bc1006f4c9bd789/37.8267,-122.423
tgtURL =  "https://api.forecast.io/forecast/" + API_KEY + "/" # LATITUDE,LONGITUDE,TIME


# Based on the data sample, create the table in a SQLite database called "weather.db".
def init_db():
	con = lite.connect('weather.db')
	cur = con.cursor()
	tgtCreateTableQuery = '''CREATE TABLE IF NOT EXISTS hourly (
		ozone REAL,
        cloudCover REAL, 
        apparentTemperature REAL, 
        precipAccumulation REAL,
        pressure REAL, 
        precipProbability REAL, 
        visibility REAL,
        precipType TEXT,
        summary TEXT, 
        icon TEXT, 
        temperature REAL, 
        dewPoint REAL, 
        humidity REAL, 
        windSpeed REAL, 
        time INT,
        precipIntensity REAL,
        windBearing INT,
        latitude REAL,
        longitude REAL,
        UNIQUE(latitude,longitude,time) ON CONFLICT REPLACE )'''
	with con:
		cur.execute(tgtCreateTableQuery)
	con.commit()
	con.close()


cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435',
            "NewYork":'40.712784,-74.005941'
        }

def init_city_table():
	con = lite.connect('weather.db')
	cur = con.cursor()
	tgtCreateTableQuery = '''CREATE TABLE IF NOT EXISTS cities ( 
		name TEXT,
        latitude REAL, 
        longitude REAL,UNIQUE(name,latitude,longitude) ON CONFLICT REPLACE )'''
	cur.execute(tgtCreateTableQuery)
	for key in cities:
		tgtInsertQuery = "INSERT into cities(name,latitude,longitude) VALUES (?,?,?)"
		cur.execute(tgtInsertQuery,(key,cities[key].split(",")[0],cities[key].split(",")[1]))

	con.commit()
	con.close()
# commented due to api limit 
# r = requests.get(tgtURL + cities["Atlanta"] + "," + curTime)
# sample data result
#tempRES = {u'hourly': {u'icon': u'partly-cloudy-night', u'data': [{u'temperature': 32.26, u'icon': u'clear-night', u'dewPoint': 23.32, u'humidity': 0.69, u'visibility': 9.58, u'summary': u'Clear', u'apparentTemperature': 32.26, u'pressure': 1025.57, u'windSpeed': 3, u'cloudCover': 0, u'time': 1417237200, u'windBearing': 180, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 31.24, u'icon': u'clear-night', u'dewPoint': 23.8, u'humidity': 0.74, u'visibility': 9.58, u'summary': u'Clear', u'apparentTemperature': 31.24, u'pressure': 1025.34, u'cloudCover': 0.07, u'time': 1417240800, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 31.03, u'icon': u'clear-night', u'dewPoint': 23.75, u'humidity': 0.74, u'visibility': 9.58, u'summary': u'Clear', u'apparentTemperature': 31.03, u'pressure': 1025.27, u'cloudCover': 0.07, u'time': 1417244400, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 30.85, u'icon': u'clear-night', u'dewPoint': 23.95, u'humidity': 0.75, u'visibility': 9.58, u'summary': u'Clear', u'apparentTemperature': 30.85, u'pressure': 1025.3, u'cloudCover': 0.07, u'time': 1417248000, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 29.85, u'icon': u'clear-night', u'dewPoint': 23.9, u'humidity': 0.78, u'visibility': 9.37, u'summary': u'Clear', u'apparentTemperature': 29.85, u'pressure': 1025, u'cloudCover': 0, u'time': 1417251600, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 29.59, u'icon': u'clear-night', u'dewPoint': 23.96, u'humidity': 0.79, u'visibility': 9.37, u'summary': u'Clear', u'apparentTemperature': 29.59, u'pressure': 1025.3, u'cloudCover': 0, u'time': 1417255200, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 29.64, u'icon': u'clear-night', u'dewPoint': 23.61, u'humidity': 0.78, u'visibility': 9.37, u'summary': u'Clear', u'apparentTemperature': 29.64, u'pressure': 1025.76, u'windSpeed': 3, u'cloudCover': 0, u'time': 1417258800, u'windBearing': 200, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 28.98, u'icon': u'clear-night', u'dewPoint': 23.73, u'humidity': 0.8, u'visibility': 9.44, u'summary': u'Clear', u'apparentTemperature': 28.98, u'pressure': 1026.18, u'cloudCover': 0, u'time': 1417262400, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 29.54, u'icon': u'clear-day', u'dewPoint': 24.43, u'humidity': 0.81, u'visibility': 8.26, u'summary': u'Clear', u'apparentTemperature': 29.54, u'pressure': 1026.85, u'windSpeed': 3, u'cloudCover': 0.15, u'time': 1417266000, u'windBearing': 200, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 35.66, u'icon': u'clear-day', u'dewPoint': 27.38, u'humidity': 0.72, u'visibility': 8.45, u'summary': u'Clear', u'apparentTemperature': 35.66, u'pressure': 1027.2, u'windSpeed': 2.78, u'cloudCover': 0.15, u'time': 1417269600, u'windBearing': 211, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 43.45, u'icon': u'clear-day', u'dewPoint': 26.48, u'humidity': 0.51, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 39.33, u'pressure': 1027.29, u'windSpeed': 6.92, u'cloudCover': 0.15, u'time': 1417273200, u'windBearing': 224, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 48.45, u'icon': u'clear-day', u'dewPoint': 25.87, u'humidity': 0.41, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 44.97, u'pressure': 1027.27, u'windSpeed': 7.77, u'cloudCover': 0.12, u'time': 1417276800, u'windBearing': 214, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 53.13, u'icon': u'partly-cloudy-day', u'dewPoint': 26.11, u'humidity': 0.35, u'visibility': 10, u'summary': u'Partly Cloudy', u'apparentTemperature': 53.13, u'pressure': 1026.22, u'windSpeed': 8.28, u'cloudCover': 0.31, u'time': 1417280400, u'windBearing': 221, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 56.32, u'icon': u'partly-cloudy-day', u'dewPoint': 26.67, u'humidity': 0.32, u'visibility': 10, u'summary': u'Partly Cloudy', u'apparentTemperature': 56.32, u'pressure': 1025.06, u'windSpeed': 6.69, u'cloudCover': 0.54, u'time': 1417284000, u'windBearing': 233, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 57.97, u'icon': u'clear-day', u'dewPoint': 27.16, u'humidity': 0.31, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 57.97, u'pressure': 1024.13, u'windSpeed': 7.72, u'time': 1417287600, u'windBearing': 214, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 58.88, u'icon': u'clear-day', u'dewPoint': 28.06, u'humidity': 0.31, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 58.88, u'pressure': 1023.53, u'windSpeed': 8.02, u'time': 1417291200, u'windBearing': 214, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 58.85, u'icon': u'partly-cloudy-day', u'dewPoint': 28.84, u'humidity': 0.32, u'visibility': 10, u'summary': u'Partly Cloudy', u'apparentTemperature': 58.85, u'pressure': 1023.04, u'windSpeed': 8.62, u'cloudCover': 0.31, u'time': 1417294800, u'windBearing': 212, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 57.95, u'icon': u'clear-day', u'dewPoint': 29.81, u'humidity': 0.34, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 57.95, u'pressure': 1023.25, u'windSpeed': 6.61, u'cloudCover': 0, u'time': 1417298400, u'windBearing': 200, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 56.24, u'icon': u'clear-night', u'dewPoint': 30.24, u'humidity': 0.37, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 56.24, u'pressure': 1023.43, u'windSpeed': 4.77, u'time': 1417302000, u'windBearing': 188, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 52.69, u'icon': u'partly-cloudy-night', u'dewPoint': 32, u'humidity': 0.45, u'visibility': 10, u'summary': u'Mostly Cloudy', u'apparentTemperature': 52.69, u'pressure': 1023.77, u'windSpeed': 5.46, u'cloudCover': 0.75, u'time': 1417305600, u'windBearing': 170, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 50.6, u'icon': u'partly-cloudy-night', u'dewPoint': 32.64, u'humidity': 0.5, u'visibility': 10, u'summary': u'Partly Cloudy', u'apparentTemperature': 50.6, u'pressure': 1023.99, u'windSpeed': 4.9, u'cloudCover': 0.31, u'time': 1417309200, u'windBearing': 183, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 50.18, u'icon': u'partly-cloudy-night', u'dewPoint': 32.93, u'humidity': 0.51, u'visibility': 10, u'summary': u'Partly Cloudy', u'apparentTemperature': 50.18, u'pressure': 1023.97, u'windSpeed': 6.84, u'cloudCover': 0.31, u'time': 1417312800, u'windBearing': 180, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 48.4, u'icon': u'clear-night', u'dewPoint': 32.45, u'humidity': 0.54, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 46.91, u'pressure': 1023.85, u'windSpeed': 4.15, u'cloudCover': 0.12, u'time': 1417316400, u'windBearing': 187, u'precipIntensity': 0, u'precipProbability': 0}, {u'temperature': 45.69, u'icon': u'clear-night', u'dewPoint': 34.01, u'humidity': 0.63, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 42.62, u'pressure': 1023.89, u'windSpeed': 5.86, u'cloudCover': 0.19, u'time': 1417320000, u'windBearing': 175, u'precipIntensity': 0, u'precipProbability': 0}], u'summary': u'Partly cloudy in the evening.'}, u'currently': {u'temperature': 43.44, u'icon': u'clear-day', u'dewPoint': 26.48, u'humidity': 0.51, u'visibility': 10, u'summary': u'Clear', u'apparentTemperature': 39.32, u'pressure': 1027.29, u'windSpeed': 6.92, u'cloudCover': 0.15, u'time': 1417273195, u'windBearing': 224, u'precipIntensity': 0, u'precipProbability': 0}, u'longitude': -84.422675, u'flags': {u'units': u'us', u'sources': [u'isd'], u'isd-stations': [u'722190-13874', u'722195-03888', u'722196-53863', u'722270-13864', u'747812-63813']}, u'daily': {u'data': [{u'apparentTemperatureMinTime': 1417262400, u'cloudCover': 0.17, u'temperatureMin': 28.98, u'summary': u'Partly cloudy in the evening.', u'dewPoint': 27.3, u'apparentTemperatureMax': 58.88, u'temperatureMax': 58.88, u'temperatureMaxTime': 1417291200, u'windBearing': 203, u'moonPhase': 0.26, u'visibility': 9.69, u'sunsetTime': 1417300252, u'pressure': 1025.02, u'precipProbability': 0, u'apparentTemperatureMin': 28.98, u'precipIntensityMax': 0, u'icon': u'partly-cloudy-night', u'apparentTemperatureMaxTime': 1417291200, u'humidity': 0.56, u'windSpeed': 5.5, u'time': 1417237200, u'precipIntensity': 0, u'sunriseTime': 1417263851, u'temperatureMinTime': 1417262400}]}, u'offset': -5, u'latitude': 33.762909, u'timezone': u'America/New_York'}

# How many levels does the data have? 
def get_max_depth_level(tgtJson):
	# if not list or dict, return one
	if not isinstance(tgtJson, dict) and not isinstance(tgtJson,list):
		return 0
	curDepth = []
	if isinstance(tgtJson, dict):
		for key in tgtJson:
			curDepth.append(get_max_depth_level(tgtJson[key])+1)
	elif isinstance(tgtJson,list):
		for curElement in tgtJson:
			curDepth.append(get_max_depth_level(curElement)+1)
	return max(curDepth)

#print "How many levels does the data have? " + str(get_max_depth_level(tempRES))
# Which field do we want to save to get the daily maximum temperature?
# for key in tempRES["hourly"]["data"]:
# 	print datetime.datetime.fromtimestamp(int(key["time"])),key["temperature"]
def update_hourly():
	con = lite.connect('weather.db')
	cur = con.cursor()
	for key in cities:
		if key != 'NewYork':
			continue
		for i in range(0,30):
			curDate = datetime.datetime.now() - datetime.timedelta(days=i)
			curTime = curDate.strftime("%Y-%m-%dT%H:%M:%S")
			curURL = tgtURL + cities[key] + "," + curTime
			r = requests.get(curURL)
			curJSON = r.json()
			for curHourly in curJSON["hourly"]["data"]:
				curHourly["latitude"] = cities[key].split(",")[0]
				curHourly["longitude"] = cities[key].split(",")[1]
				print getInsertFromDict(curHourly)
				cur.execute(getInsertFromDict(curHourly))
		break
	con.commit()
	con.close()

def getInsertFromDict(tgtJson):
	tgtKeyList = []
	tgtValueList = []
	for key in tgtJson:
		tgtKeyList.append(key)
		if isinstance(tgtJson[key],unicode):
			tgtValueList.append("'" + str(tgtJson[key]) + "'")
		else:
			tgtValueList.append(str(tgtJson[key]))
	tgtInsertQuery = "INSERT INTO hourly(" + ",".join(tgtKeyList) + ")"
	tgtInsertQuery += " VALUES (" + ",".join(tgtValueList) + ")"
	return  tgtInsertQuery

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d
init_db()
init_city_table()
update_hourly()
# Write a script that takes each city and queries every day for the past 30 days 
# (Hint: You can use the datetime.timedelta(days=1) to increment the value by day) 
# update_hourly()
# Save the max temperature values to the table, keyed on the date. 
# You can leave the date in Unix time or convert to a string. 
tgtQuery = "select distinct latitude,longitude, max(temperature) as temperature ,time  from hourly group by latitude,longitude"

#tgtQuery = "select * from hourly where  latitude = 40.712784 and longitude = -74.005941 order by time desc;"
con = lite.connect('weather.db')

df = pd.read_sql(tgtQuery,con) # can't we use this reading the query
print "Maximum temperature in last 30 days "+str(df['temperature'].tolist()[0])

# check the database and plot temp variation over time
hrlyQuery =  "select * from hourly order by time"
df_hrly = pd.read_sql(hrlyQuery, con)
plt.figure()
plt.plot(df_hrly['time'], df_hrly['temperature'], color = 'green')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature variation in NewYork city for last 30 days')
plt.savefig('/Users/shubhabrataroy/Desktop/Thinkful/Data/NYTemp30days.jpg')
