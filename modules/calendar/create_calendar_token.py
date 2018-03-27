from __future__ import print_function

import sys

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# We only need read-only access to a user's calendar
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'daily status printer'
CREDENTIAL_PATH = 'calendar-api-credentials.json'


# Gets valid user credentials using a client secret and stores them to disk ------------------
def create_credentials():
    store = Storage(CREDENTIAL_PATH)

    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
        tools.run_flow(flow, store, flags)
    else:   # Needed only for compatibility with Python 2.6
        tools.run(flow, store)
    print('Storing credentials to ' + CREDENTIAL_PATH)


def get_credentials():
    # this method gets called from the main directory of the program, prepend path
    store = Storage('modules/calendar/' + CREDENTIAL_PATH)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print("Error: Could not load Google calendar credentials. Make sure you have a valid "
              + CREDENTIAL_PATH + " file. If this file is missing, run the 'create_calendar_token.py' script.")
        sys.exit(-1)
    return credentials


if __name__ == '__main__':
    create_credentials()
