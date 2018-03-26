import requests
import datetime
import config


class _Article:

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.description = kwargs.get('description') if kwargs.get('description') != '' else None
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

        if r.status_code != 200:
            print("Error: Couldn't fetch news articles (request failed)")
            return

        try:
            json = r.json()
        except ValueError as e:
            print(e)
            print("Error: Couldn't fetch headlines (invalid or missing response content)")
            return

        try:
            articles = [_Article(**current) for current in json['articles']][0:self.count]
        except KeyError as e:
            print(e)
            print("Error: Couldn't fetch headlines (unexpected response format)")
            return

        for a in articles:
            # only print the headline
            # TODO: implement QR-Code generation
            print(a.title)
