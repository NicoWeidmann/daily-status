import requests
from util import calculate_target_date, print_header, print_error
import config

# set locale to german
import locale
locale.setlocale(locale.LC_ALL, config.LOCALE)


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

        print_header(printer, 'Wetter')

        if r.status_code != 200:
            print("Error: Couldn't reach darksky API for weather information")
            print_error(printer)
            return

        json = r.json()

        # calculate UNIX timestamp of the data that should be extracted from the response
        # TODO: make sure this works with all time zones
        target_date = calculate_target_date()
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
            print_error()
            return

        forecast_text = ("{summary} Die Temperatur beträgt zwischen {temperatureLow}°C "
                         "und {temperatureHigh}°C. Die Niederschlagswahrscheinlichkeit beträgt {precipProbability}%.")

        try:
            # calculate percentage
            forecast_data['precipProbability'] *= 100

            # insert weather data into format string
            forecast_text = forecast_text.format(**forecast_data)
        except KeyError:
            print("Error: acquired weather data is missing some required attributes")
            print_error()
            return

        printer.write(forecast_text)
        printer.feed(2)
