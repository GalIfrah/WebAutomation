import sys
import json
from App import PageObjects

from App.SutTests import *


class App:

    name = None
    config = None
    platform = None
    env = None


    def __init__(self):

        if len(sys.argv) != 0:
            self.name = sys.argv.pop(1)
            self.env = sys.argv.pop(1)
            self.platform = sys.argv.pop(1)


        self.validateApp()
        self.validatePlatform()
        self.validateEnv()
        self.setConfig()
        self.setPlatform()
        self.setEnv()


    def validateApp(self):
        if self.name == 'FM':
            return

        if self.name == 'TRG':
            return

        if self.name == 'ML':
            return

        raise Exception('`' + self.name + '` is not a valid app name')


    def validatePlatform(self):
        if self.platform == 'mobile':
            return

        if self.platform == 'desktop':
            return

        raise Exception('`' + self.mobile + '` is not a valid platform')


    def validateEnv(self):
        if self.env == 'test':
            return

        if self.env == 'sendbox':
            return

        if self.env == 'prod':
            return

        raise Exception('`' + self.env + '` is not a valid environment')


    def setConfig(self):
        with open(self.name + '.json') as data_file:
            data = json.load(data_file)

        self.config = data


    def setPlatform(self):
        BasicTestClass.platform = self.platform


    def setEnv(self):
        PageObjects.env = self.env


# end of Environment class


app = App()

print("===================================")
print('Running on ' + app.name + '_' + app.platform + ' App')
print("===================================")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
