import requests
import sys
import datetime
try:
    import config
except ImportError as e:
    # config file is missing
    print('Error:', e)
    print('Please create a config file'
          ' (see "config_example.py" for instructions on how to do this) and restart the program.')
    sys.exit(1)

# set locale to german
import locale
locale.setlocale(locale.LC_ALL, 'de_DE')


class Weather:

    # this is the API base url for any requests
    API_BASE = 'https://api.darksky.net/forecast'

    # these parameters are passed on each API call
    params = {'exclude': 'currently,minutely,hourly,alerts,flags',
              'lang': 'de',
              'units': 'si'}

    def __init__(self, lat, long):
        # for request format see https://darksky.net/dev/docs
        self.api_url = "{}/{}/{},{}".format(Weather.API_BASE,
                                            config.DARKSKY_KEY, lat, long)

    def execute(self, printer):
        # perform API request
        r = requests.get(self.api_url, params=self.params)

        if r.status_code != 200:
            print("Error: Couldn't reach darksky API for weather information")
            return

        json = r.json()

        # calculate UNIX timestamp of the data that should be extracted from the response
        # TODO: make sure this works with all time zones
        target_date = datetime.datetime.now()
        target_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
        if datetime.datetime.time(datetime.datetime.now()) >= config.TIME_LIMIT:
            # we print information for the next day
            target_date += datetime.timedelta(days=1)

        timestamp = target_date.timestamp()

        forecast_data = None
        for current_day in json['daily']['data']:
            if current_day['time'] == timestamp:
                # found correct day
                forecast_data = current_day
                break
        else:
            # couldn't find appropriate data for the desired day
            print("Error: Couldn't acquire weather data for", target_date.isoformat)
            return

        forecast_text = ("Wettervorhersage für {:%A}: {summary} Die Temperatur beträgt zwischen {temperatureLow}°C "
                         "und {temperatureHigh}°C. Die Niederschlagswahrscheinlichkeit beträgt {precipProbability}%.")

        # calculate percentage
        try:
            forecast_data['precipProbability'] *= 100
            forecast_text = forecast_text.format(target_date, **forecast_data)
        except KeyError:
            print("Error: acquired weather data is missing some required attributes")
            forecast_text = "Es ist ein Fehler beim Laden des Wetters aufgetreten."

        print(forecast_text)
