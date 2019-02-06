import json
import HtmlTestRunner
import sys


class SUT:
    name = None
    config = None
    platform = None
    env = None
    reportType = None

    def __init__(self):

        if len(sys.argv) != 0:
            # self.name = sys.argv.pop(1)
            # self.env = sys.argv.pop(1)
            # self.platform = sys.argv.pop(1)
            # self.reportType = sys.argv.pop(1)

            self.name = "FM"
            self.env = "test"
            self.platform = "desktop"
            self.reportType = "png"

        self.validateApp()
        self.validatePlatform()
        self.validateEnv()
        self.setConfig()
        self.setPlatform()
        self.setEnv()
        self.setReports()

    def validateApp(self):
        if self.name == 'FM':
            return

        if self.name == 'TRG':
            return

        if self.name == 'ML':
            return

        if self.name == 'NOVEL':
            return

        if self.name == 'BRAZ':
            return

        if self.name == 'BL':
            return

        raise Exception('`' + self.name + '` is not a valid app name')

    def validatePlatform(self):
        if self.platform == 'mobile':
            return

        if self.platform == 'desktop':
            return

        raise Exception('`' + self.platform + '` is not a valid platform')

    def validateEnv(self):
        if self.env == 'test':
            return

        if self.env == 'sendbox':
            return

        if self.env == 'prod':
            return

        raise Exception('`' + self.env + '` is not a valid environment')

    def setConfig(self):

        import App.PageObjects
        with open("AppsConfigurations\\" + self.name + '.json') as data_file:
            App.PageObjects.params = json.load(data_file)

    def setPlatform(self):
        from Infrastructure.BasicTest import BasicTestClass
        BasicTestClass.platform = self.platform

    def setEnv(self):

        import App.PageObjects
        App.PageObjects.env = self.env

    def setReports(self):

        from Infrastructure.BasicTest import BasicTestClass
        BasicTestClass.reporterType = self.reportType
        BasicTestClass.appName = self.name

        from Services import EmailService
        EmailService.appName = self.name




sut = SUT()

# from SutTests.TestsClassesInit import *
# from SutTests.FlowsTests import *
from SutTests.DemoTests import *
# from SutTests.ConnectTests import *
# from SutTests.WalletTests import *
# from SutTests.EnterPhoneScreenTests import *
# from SutTests.MenuTests import *


print("===================================")
print('Running on ' + sut.name + '_' + sut.platform + ' App')
print("===================================")

if __name__ == '__main__':
    from Services import EmailService
try:

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='htmlReports'))

except:

    time.sleep(3)
    EmailService.emailReporting(sut.reportType)



