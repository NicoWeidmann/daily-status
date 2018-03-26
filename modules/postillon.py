import requests


class Ticker:

    TICKER_URL = 'http://www.der-postillion.de/ticker/newsticker2.php'

    def __init__(self, count):
        self.count = count

    def execute(self, printer):
        r = requests.get(Ticker.TICKER_URL)
        if r.status_code != 200:
            print("Error: Couldn't load postillon tickers (request failed)")
            return

        try:
            json = r.json()
        except ValueError as e:
            print(e)
            print("Error: Couldn't fetch tickers (invalid or missing response content)")
            return

        try:
            # extract ticker texts from response, trim to at max self.count tickers
            tickers = [ticker['text'] for ticker in json['tickers']][0:self.count]
        except KeyError as e:
            print(e)
            print("Error: Couldn't fetch tickers (unexpected response format)")
            return

        for ticker in tickers:
            print('+++ ' + ticker + ' +++')
