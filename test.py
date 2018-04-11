from modules import greeter
from modules.calendar import googlecalendar as cal
from modules import weather
from modules import postillon
from lib.printer.Adafruit_Thermal import Adafruit_Thermal


printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
modules = [greeter.Greeter(name='Nico'),
           cal.Calendar(),
           weather.Weather(lat=49.0159405, long=8.339494),
           postillon.Ticker(count=2)]

{module.execute(printer) for module in modules}
