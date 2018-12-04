import sys
import unittest
import json


class App():
    name = None
    config = None

    def __init__(self):
        if len(sys.argv) > 1:
            self.name = sys.argv.pop(1)

        self.validateEnv()
        self.setConfig()

    def validateEnv(self):
        if self.name == 'FM':
            return

        if self.name == 'sandbox':
            return

        if self.name == 'prod':
            return

        raise Exception('`' + self.name + '` is not a valid environment')

    def setConfig(self):
        with open(self.name + '.json') as data_file:
            data = json.load(data_file)

        self.config = data


# end of Environment class

app = App()

from FrancoManca.FmTests import *

print("===================================")
print('Running on ' + app.name + ' App')
print("===================================")

if __name__ == '__main__':
    unittest.main()