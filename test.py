from modules import greeter
from modules.calendar import googlecalendar as cal
from lib.printer.Adafruit_Thermal import Adafruit_Thermal


printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
modules = [greeter.Greeter(name='Nico'), cal.Calendar()]

{module.execute(printer) for module in modules}
