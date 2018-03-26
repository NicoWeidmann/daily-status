from util import calculate_target_date


class Greeter:

    def __init__(self, name):
        self.name = name

    def execute(self, printer):
        print('Hallo {0}, hier ist dein Status für {1:%A}, den {1:%x}'.format(self.name, calculate_target_date()))
