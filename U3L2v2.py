import requests
import sqlite3 as lite
import datetime

api_key = "dc499171e079785818999b024c17fe40"
url = 'https://api.forecast.io/forecast/' + api_key + "/"
cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

'''by setting this equal to a variable, we fix the calculation to the point when we started the scrip 
(rather than have things move around while we're coding.)'''
end_date = datetime.datetime.now()

#creating the database
con = lite.connect('/home/sroy/Desktop/Thinkful/Exercises/weather.db')
cur = con.cursor()
cities.keys()
with con:
    cur.execute("DROP TABLE IF EXISTS daily_temp")
    cur.execute('CREATE TABLE daily_temp(day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);')


query_date = end_date - datetime.timedelta(days=30) #the current value being processed
with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)


#loop through the cities and query the api
for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime("%Y-%m-%dT%H:%M:%S"))

        with con: #inrsert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))
        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day

con.close() # a good practice to close connection to database
