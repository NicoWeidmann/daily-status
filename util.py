import datetime
import config


# calculate the date the report should be generated for.
# The date depends on the value set in config.TIME_LIMIT and the current system time.
def calculate_target_date():
    target_date = datetime.datetime.now(tz=datetime.timezone(config.UTC_OFFSET))
    target_date = target_date.replace(hour=0, minute=0, second=0, microsecond=0)
    if datetime.datetime.time(datetime.datetime.now()) >= config.TIME_LIMIT:
        # we print information for the next day
        target_date += datetime.timedelta(days=1)
    return target_date


# return a sorting key for a given event as specified by the Google Calendar API
# formatted as ISO 8601 string.
# This places whole day events before timed events
# TODO: consider timezone (e.g. convert to UTC)
def sortkey_event_datetime(event):
    return event['start'].get('dateTime', event['start'].get('date'))


def print_header(printer, header):
    printer.justify('C')
    printer.inverseOn()
    printer.write('--- {} ---\n'.format(header))
    printer.inverseOff()
    printer.justify('L')
    printer.feed(1)


def print_error(printer):
    printer.justify('C')
    printer.write('Es ist ein Fehler aufgetreten :(')
    printer.justify('L')
    printer.feed(2)
