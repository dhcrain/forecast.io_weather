import os
import datetime
import requests
import geocoder
from terminaltables import AsciiTable
import click

"""
Powered by Dark Sky - https://darksky.net/poweredby/
"""

""" Put your forecast.io API key here """
DARKSKY_API_KEY = os.environ['forecast_api']

""" UNITS "us" for °F or "si" for °C """
UNITS = "us"
UNIT_LETTER = "°F" if UNITS == "us" else "°C"


class colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def readable_time(time):
    return str(datetime.datetime.fromtimestamp(int(time)).strftime('%-I%p')).lower()


def temp_format(color, number):
    return color + str(int(number)) + UNIT_LETTER + colors.ENDC


@click.command()
@click.option('--location', '-l', help='Enter a location, Zip Code (28768)')
def get_weather(location):

    if location is None:
        g = geocoder.ip('me')
    else:
        g = geocoder.google(location)

    url = "https://api.darksky.net/forecast/{}/{},{}?exclude=minutely,hourly,alerts,flags?UNITS={}".format(DARKSKY_API_KEY, g.lat, g.lng, UNITS)
    response = requests.get(url).json()
    table_week = [["", "", "HI", "at", "LO", "at", "", ""]]

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

    table_week[1][0] = colors.BOLD + colors.GREEN + "* Today *" + colors.ENDC

    title = colors.BOLD + " {}, {} - Current Temp: {} ".format(g.city, g.state, (str(int(response['currently']['temperature'])) + UNIT_LETTER)) + colors.ENDC

    # AsciiTable
    table_instance = AsciiTable(table_week, title)
    table_instance.justify_columns[2] = 'right'

    # Output
    print("\n" + colors.BOLD + response['daily']['summary'] + colors.ENDC + "\n")
    print(table_instance.table)


if __name__ == '__main__':
    get_weather()
