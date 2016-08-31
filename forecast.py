import datetime
import os
import requests
import geocoder
from tabulate import tabulate

forecast_api_key = os.environ['forecast_api']

print("Enter a location, Zip Code (28768) *OR* City, State (Greenville, SC)")
location = input("Location? ")
g = geocoder.google(location)

url = "https://api.forecast.io/forecast/{}/{},{}".format(forecast_api_key, g.latlng[0], g.latlng[1])
response = requests.get(url).json()
table_week = []
print("\n" + response['daily']['summary'])
for day in response['daily']['data']:
    time = datetime.datetime.fromtimestamp(int(day['time'])).strftime('%a %b %-d')
    summary = day['summary']
    max_temp = str(int(day['temperatureMax'])) + "°F"
    max_temp_time = "at " + str(datetime.datetime.fromtimestamp(int(day['temperatureMaxTime'])).strftime('%-I%p'))
    min_temp = str(int(day['temperatureMin'])) + "°F"
    min_temp_time = "at " + str(datetime.datetime.fromtimestamp(int(day['temperatureMinTime'])).strftime('%-I%p'))
    percip_chance = str(int(day['precipProbability'] * 100)) + "%"
    try:
        percip_type = "of " + day['precipType']
    except KeyError:
        percip_type = " "
#     print("""
# {} - {}
# * h: {}°F at {} * l: {}°F at {} * {}% {}""".format(time, summary, max_temp, max_temp_time, min_temp, min_temp_time, percip_chance, percip_type))
    table_day = [time, summary, max_temp, max_temp_time, min_temp, min_temp_time, percip_chance, percip_type]
    table_week.append(table_day)

table_week[0][0] = "* Today *"

headers = ["", "", "HI", "", "LO", "", "", ""]
print(tabulate(table_week, headers=(headers), tablefmt="simple"))
