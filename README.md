# Weather from Dark Sky API

CLI to get weekly forecast from forecast.io

You will need an API key from https://darksky.net/dev/  
It's __free__ for 1000 API calls per day.

Can add it to your environment variable or just paste it in for the value of `darksky_api_key`

## Options
- Get location from your ip address
- Enter location manually, zip or city, state

Just comment out / delete the option that you don't want to use.

__Units__
- Set `units = ` "us" for °F or "si" for °C

### To run:
- `git clone https://github.com/dhcrain/forecast.io_weather.git`
- `pip install requirements.txt`
- `python forecast.py`


Tested in Python 3.5.1 / OSX  
Powered by Dark Sky - https://darksky.net/poweredby/
