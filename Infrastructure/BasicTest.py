from Infrastructure.WebDriverWrapper import Wrapper
from App.PageObjects import *
from Utils import EmailService
import os
from time import sleep


class BasicTestClass:


    driver = Wrapper()
    platform = ''
    testName = ''
    reporterType = ''
    appName = ''


    @classmethod
    def setUpClass(cls):
            # pass
            os.system("C:\WINDOWS\system32\cmd.exe /C start C:\\Users\galif\Desktop\MyStuff\Programming\Selenium\startGrid.bat")

            os.system("C:\WINDOWS\system32\cmd.exe /C start C:\\Users\galif\Desktop\MyStuff\Programming\Selenium\startNode.bat")


    def setUp(self):

        if self.platform == "desktop":
            sleep(3)

            print('init the remote webdriver')
            print(BasicTestClass.platform)
            self.testName = self._testMethodName
            BasicTestClass.driver.initDesktop('http://localhost:4444/wd/hub')


        if self.platform == "mobile":
            sleep(3)
            print('init the mobile remote webdriver')
            self.testName = self._testMethodName
            # BasicTestClass.driver.initMobile('http://galifrah4:N4XNKDnwH5ipipycghhp@hub.browserstack.com:80/wd/hub')

            # for local host
            BasicTestClass.driver.initMobile('http://localhost:4444/wd/hub')

    def tearDown(self):

            self.driver.saveScreenShot(0, self.testName)
            print('test ended')
            print('**************************************')
            self.driver.closeCurrent()


    @classmethod
    def tearDownClass(cls):

        pass
