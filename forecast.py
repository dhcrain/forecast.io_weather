import os
import datetime
import requests
import geocoder
from tabulate import tabulate

"""
Powered by Dark Sky - https://darksky.net/poweredby/
"""

""" Put your forecast.io API key here """
forecast_api_key = os.environ['forecast_api']

""" UNITS "us" for °F or "si" for °C """
units = "us"

""" To get Location automatically from ip address """
g = geocoder.ip('me')

""" To get manual input for location """
# print("Enter a location, Zip Code (28768) *OR* City, State (Greenville, SC)")
# location = input("Location? ")
# g = geocoder.google(location)


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

if units == "us":
    unit_letter = "°F"
else:
    unit_letter = "°C"


def readable_time(time):
    return str(datetime.datetime.fromtimestamp(int(time)).strftime('%-I%p')).lower()


def temp_format(color, number):
    return color + str(int(number)) + unit_letter + colors.ENDC


def get_weather():
    url = "https://api.darksky.net/forecast/{}/{},{}?exclude=minutely,hourly,alerts,flags?units={}".format(forecast_api_key, g.latlng[0], g.latlng[1], units)
    response = requests.get(url).json()
    table_week = []
    for day in response['daily']['data']:
        date = datetime.datetime.fromtimestamp(int(day['time'])).strftime('%a %b %-d')
        summary = day['summary']
        max_temp = temp_format(colors.RED, day['temperatureMax'])
        max_temp_time = readable_time(day['temperatureMaxTime'])
        min_temp = temp_format(colors.BLUE, day['temperatureMin'])
        min_temp_time = readable_time(day['temperatureMinTime'])
        percip_chance = str(int(day['precipProbability'] * 100)) + "%"
        try:
            percip_type = day['precipType'].title()
        except KeyError:
            percip_type = ""
        table_day = [date, summary, max_temp, max_temp_time, min_temp, min_temp_time, percip_chance, percip_type]
        table_week.append(table_day)

    table_week[0][0] = colors.GREEN + "* Today *" + colors.ENDC
    headers = ["", "", "HI", "at", "LO", "at", "", ""]
    print("\nForecast for: {}, {}".format(g.city, g.state))
    print(colors.UNDERLINE + "Current Temp" + colors.ENDC + ": " + str(int(response['currently']['temperature'])) + unit_letter)
    print("\n" + colors.BOLD + response['daily']['summary'] + colors.ENDC)
    print(tabulate(table_week, headers=(headers), tablefmt="simple"))

if __name__ == '__main__':
    get_weather()
