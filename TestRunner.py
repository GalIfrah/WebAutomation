import sys
import json
import HtmlTestRunner
# Test Classes
import buf as buf

from App.SutTests import *


class App:
    name = 'FM'
    config = None

    def __init__(self):
        if len(sys.argv) > 1:
            self.name = sys.argv.pop(1)

        self.validateEnv()
        self.setConfig()

    def validateEnv(self):
        if self.name == 'FM':
            return

        if self.name == 'TRG':
            return

        if self.name == 'ML':
            return

        raise Exception('`' + self.name + '` is not a valid environment')

    def setConfig(self):
        with open(self.name + '.json') as data_file:
            data = json.load(data_file)

        self.config = data


# end of Environment class

app = App()

print("===================================")
print('Running on ' + app.name + ' App')
print("===================================")

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
