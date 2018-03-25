import requests
import config


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
        r = requests.get(self.api_url, params=self.params)
        print(r.text)
