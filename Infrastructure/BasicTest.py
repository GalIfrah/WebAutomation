from Infrastructure.WebDriverWrapper import Wrapper
from App.PageObjects import *


class BasicTestClass:

    driver = Wrapper()
    platform = ''
    testName = ''


    def setUp(self):

        if self.platform == "desktop":
            print('init the remote webdriver')
            print(BasicTestClass.platform)
            self.testName = self._testMethodName
            BasicTestClass.driver.initDesktop('http://localhost:4444/wd/hub')

        if self.platform == "mobile":
            print('init the mobile remote webdriver')
            BasicTestClass.driver.initMobile('http://localhost:4444/wd/hub', 'iPhone X')


    def tearDown(self):

        self.driver.saveScreenShot(0, self.testName)
        print('test ended')
        print('**************************************')
        self.driver.closeCurrent()
