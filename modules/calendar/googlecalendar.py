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

        # load all available calendars of the authenticated user
        calendars = []

        # we loop until no nextPageToken is returned, as this indicates that no more pages exist
        currentResult = {'nextPageToken': None}
        while 'nextPageToken' in currentResult:
            currentResult = self.cal_service.calendarList().list(pageToken=currentResult['nextPageToken']).execute()
            # we only need the calendar IDs
            calendars.extend([item.get('id') for item in currentResult.get('items', [])])

        if len(calendars) == 0:
            # no calendars found, therefore no events can exist
            return

        # we want to load events for the current (or next) day
        startTime = util.calculate_target_date()
        endTime = startTime + datetime.timedelta(days=1)

        # correctly format times for the request
        startTime, endTime = startTime.isoformat(), endTime.isoformat()

        # load events using the Google API
        events = []  # we will accumulate the events of all calendars in this list
        for calendar in calendars:
            # again looping so that we do not miss events when events are returned on more than one page
            eventsResult = {'nextPageToken': None}
            while 'nextPageToken' in eventsResult:
                eventsResult = self.cal_service.events().list(
                    calendarId=calendar, timeMin=startTime, timeMax=endTime, singleEvents=True,
                    orderBy='startTime', pageToken=eventsResult['nextPageToken']).execute()
                events.extend(eventsResult.get('items', []))

        # print events
        for event in sorted(events, key=util.sortkey_event_datetime):
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
