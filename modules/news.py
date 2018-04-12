import requests
import datetime
import config
import util


class _Article:

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.description = kwargs.get('description') if kwargs.get('description') != '' else None
        self.source_name = kwargs.get('source').get('name')
        self.url = kwargs.get('url')

        # we parse the date as ISO 8601 in UTC
        self.pubDate = datetime.datetime.strptime(kwargs.get('publishedAt'), '%Y-%m-%dT%H:%M:%SZ')
        self.pubDate.replace(tzinfo=datetime.timezone.utc)
        self.pubDate.astimezone()   # transform date to match local time zone


class News:

    API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'

    def __init__(self, count):
        self.count = count

    def execute(self, printer):
        # currently we fetch top buzzfeed articles (don't judge me, they are a good laugh)
        params = {'sources': 'buzzfeed', 'pageSize': self.count}
        r = requests.get(News.API_ENDPOINT, params=params, headers={'Authorization': 'Bearer ' + config.NEWSAPI_KEY})

        util.print_header(printer, 'Nachrichten')

        if r.status_code != 200:
            print("Error: Couldn't fetch news articles (request failed)")
            util.print_error(printer)
            return

        try:
            json = r.json()
        except ValueError as e:
            print(e)
            print("Error: Couldn't fetch headlines (invalid or missing response content)")
            util.print_error(printer)
            return

        try:
            articles = [_Article(**current) for current in json['articles']][0:self.count]
        except KeyError as e:
            print(e)
            print("Error: Couldn't fetch headlines (unexpected response format)")
            util.print_error(printer)
            return

        for a in articles:
            # print the source
            printer.underlineOn()
            printer.write(a.source_name + '\n')
            printer.underlineOff()
            # print the headline
            printer.write(a.title + '\n')
            printer.feed(1)
            # TODO: implement QR-Code generation

        printer.feed(1)
