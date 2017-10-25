# Weather from Dark Sky API

CLI to get weekly forecast from forecast.io

You will need an API key from https://darksky.net/dev/  
It's __free__ for 1000 API calls per day.

Can add it to your environment variable or just paste it in for the value of `darksky_api_key`

## Options
- Get location from your ip address
- Enter location manually, zip or city, state

__Units__
- Set `units = ` "us" for °F or "si" for °C

### To run:
- Create Python 3 virtual environment
- `git clone https://github.com/dhcrain/forecast.io_weather.git`
- `pip install -r requirements.txt`
- Put DarkSky API key in file or as an environment variable `forecast_api`
- `python forecast.py`
    - this will get your location from your ip address
- `python forecast.py -l <location>`
    - tell the program what location you want to see the forecast
    - <location> can be a zip code, city & state, specific address


Tested in Python 3.6.3 / OSX  
Powered by Dark Sky - https://darksky.net/poweredby/
