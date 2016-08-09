import datetime
import os
import requests
import geocoder

print("Enter a location, Zip Code (28768) * OR * City, State (Greenville, SC)")
location = input("Location? ")
g = geocoder.google(location)

api_key = os.environ['forecast_api']

lat = g.latlng[0]
lng = g.latlng[1]

url = "https://api.forecast.io/forecast/{}/{},{}".format(api_key, lat, lng)
response = requests.get(url).json()

print("\n" + response['daily']['summary'])
for day in response['daily']['data']:
    time = datetime.datetime.fromtimestamp(int(day['time'])).strftime('%A %B %-d')
    summary = day['summary']
    max_temp = int(day['temperatureMax'])
    max_temp_time = datetime.datetime.fromtimestamp(int(day['temperatureMaxTime'])).strftime('%-I%p')
    min_temp = int(day['temperatureMin'])
    min_temp_time = datetime.datetime.fromtimestamp(int(day['temperatureMinTime'])).strftime('%-I%p')
    percip_chance = int(day['precipProbability'] * 100)
    try:
        percip_type = "of " + day['precipType']
    except KeyError:
        percip_type = ""
    print("""
{} - {}
* h: {}F at {} * l: {}F at {} * {}% {}""".format(time, summary, max_temp, max_temp_time, min_temp, min_temp_time, percip_chance, percip_type))
