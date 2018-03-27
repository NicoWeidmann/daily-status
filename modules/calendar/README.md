# Instructions for using the calendar module

In order to use the calendar module, the following steps have to be completed:

### 1. Activate Google Calendar API
We have to activate the Google Calendar API for a Google API Console project that we have access to. We can either create a new project or activate the API for an existing one.

This [wizard](https://console.developers.google.com/start/api?id=calendar) can be used to either create a new project or activate the API for an existing one.  
Make sure to fill out the necessary fields in the _OAuth consent screen_ before creating the credentials.

### 2. Obtain client secret file for the API
 After creating your credentials, download them using the download button on the right side. Place the downloaded file in the same directory as this README file and rename it to `client_secret.json`.

### 3. Authenticate a user with the application (to be able to load the user's events)
Run the script `create_calendar_token.py`. It will open a browser window, in which you have to log in your Google account. This will allow the main program to access your Google calendar.

If you want to print the calendar for a different user at a later point in time, simply delete the file `calendar-api-credentials.json` and re-run the script.
