import requests
import util


class Ticker:

    TICKER_URL = 'http://www.der-postillion.de/ticker/newsticker2.php'

    def __init__(self, count):
        self.count = count

    def _print_error(printer):
        printer.justify('C')
        printer.write('Es ist ein Fehler aufgetreten :(')
        printer.justify('L')

    def execute(self, printer):
        r = requests.get(Ticker.TICKER_URL)
        util.print_header('Postillon')
        if r.status_code != 200:
            print("Error: Couldn't load postillon tickers (request failed)")
            Ticker._print_error(printer)
            return

        try:
            json = r.json()
        except ValueError as e:
            print(e)
            print("Error: Couldn't fetch tickers (invalid or missing response content)")
            Ticker._print_error(printer)
            return

        try:
            # extract ticker texts from response, trim to at max self.count tickers
            tickers = [ticker['text'] for ticker in json['tickers']][0:self.count]
        except KeyError as e:
            print(e)
            print("Error: Couldn't fetch tickers (unexpected response format)")
            Ticker._print_error(printer)
            return

        for ticker in tickers:
            print(ticker)
            printer.feed(1)

        printer.feed(1)
