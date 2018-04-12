from modules import greeter
from modules.calendar import googlecalendar as cal
from modules import weather
from modules import postillon
from modules import news

from lib.printer.Adafruit_Thermal import Adafruit_Thermal

import sys

try:
    import config
except ImportError as e:
    # config file is missing
    print('Error:', e)
    print('Please create a config file'
          ' (see "config_example.py" for instructions on how to do this) and restart the program.')
    sys.exit(1)


# you might need to set the correct baud rate and path for your printer
printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

modules = [greeter.Greeter(name=config.NAME),
           cal.Calendar(),
           weather.Weather(lat=49.0159405, long=8.339494),  # coordinates of Karlsruhe, Germany. Feel free to customize
           news.News(count=3),
           postillon.Ticker(count=3)]

{module.execute(printer) for module in modules}

# we feed a little more to have some space at the bottom when removing the paper from the printer
printer.feed(2)
