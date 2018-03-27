from modules.calendar import create_calendar_token as token
import httplib2
from apiclient import discovery

import util
import datetime


class Calendar:

    # we only need read-only access to a user's calendars
    _API_SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def __init__(self):
        # initialize google API service
        credentials = token.get_credentials()  # this will fail if no credentials are available
        http = credentials.authorize(httplib2.Http())
        self.cal_service = discovery.build('calendar', 'v3', http=http)

    def execute(self, printer):

        # we want to load events for the current (or next) day
        startTime = util.calculate_target_date()
        endTime = startTime + datetime.timedelta(days=1)

        # correctly format times for the request
        # TODO: correctly translate to UTC
        startTime, endTime = startTime.isoformat(), endTime.isoformat()

        # load events using the Google API
        eventsResult = self.cal_service.events().list(
            calendarId='primary', timeMin=startTime, timeMax=endTime, singleEvents=True,
            orderBy='startTime').execute()
        events = eventsResult.get('items', [])

        # print events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
