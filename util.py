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
