from util import calculate_target_date


class Greeter:

    def __init__(self, name):
        self.name = name

    def execute(self, printer=None):
        if printer is not None:
            # we have a printer, might as well use it
            printer.write('Hallo ')
            printer.boldOn()
            printer.write(self.name)
            printer.boldOff()
            printer.write('. Hier ist dein Status fuer\n')
            printer.justify('C')
            printer.setSize('L')
            printer.write('{:%A}\n'.format(calculate_target_date()))
            printer.setSize('S')    # this is the default size
            printer.write('{:%x}\n'.format(calculate_target_date()))
            printer.justify('L')
            printer.feed(2)
        else:
            # we have no printer, print to stdout
            print('Hallo {0}, hier ist dein Status für {1:%A}, den {1:%x}'.format(self.name, calculate_target_date()))
