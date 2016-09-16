import datetime
import os
import requests
import geocoder
from tabulate import tabulate

forecast_api_key = os.environ['forecast_api']

g = geocoder.ip('me')
# print(ip.lat)
# print(ip.lng)


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def readable_time(time):
    return str(datetime.datetime.fromtimestamp(int(time)).strftime('%-I%p'))


# print("Enter a location, Zip Code (28768) *OR* City, State (Greenville, SC)")
# location = input("Location? ")
# g = geocoder.google(location)


def get_weather():
    url = "https://api.forecast.io/forecast/{}/{},{}".format(forecast_api_key, g.latlng[0], g.latlng[1])
    response = requests.get(url).json()
    table_week = []
    for day in response['daily']['data']:
        date = datetime.datetime.fromtimestamp(int(day['time'])).strftime('%a %b %-d')
        summary = day['summary']
        max_temp = colors.RED + str(int(day['temperatureMax'])) + "°F" + colors.ENDC
        max_temp_time = "at " + readable_time(day['temperatureMaxTime'])
        min_temp = colors.BLUE + str(int(day['temperatureMin'])) + "°F" + colors.ENDC
        min_temp_time = "at " + readable_time(day['temperatureMinTime'])
        percip_chance = str(int(day['precipProbability'] * 100)) + "%"
        try:
            percip_type = "of " + day['precipType']
        except KeyError:
            percip_type = " "
        table_day = [date, summary, max_temp, max_temp_time, min_temp, min_temp_time, percip_chance, percip_type]
        table_week.append(table_day)

    table_week[0][0] = colors.GREEN + "* Today *" + colors.ENDC
    headers = ["Day", "", "HI", "", "LO", "", "", ""]
    print("\nForecast for: {}, {}".format(g.city, g.state))
    print("\n" + colors.BOLD + response['daily']['summary'] + colors.ENDC)
    print(tabulate(table_week, headers=(headers), tablefmt="simple"))

if __name__ == '__main__':
    get_weather()
