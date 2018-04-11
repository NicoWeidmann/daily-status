from datetime import time, timedelta

# this is the time during a day after which information for the next day
# will be printed instead of the current day
# format as 'HH, MM, SS'
TIME_LIMIT = time(18, 00, 00)

# this is the UTC offset of your local timezone (used for UTC conversion in some modules)
# TODO: find a more convenient solution to consider DST / different time zones
UTC_OFFSET = timedelta(hours=2)

# this is the locale used for formatting dates and times in the status
LOCALE = 'de_DE.utf8'

# this is the API key used for the darksky.net weather API
DARKSKY_KEY = 'YOUR API KEY HERE'

# this is the API key used for the newsapi.org news API
NEWSAPI_KEY = 'YOUR API KEY HERE'
