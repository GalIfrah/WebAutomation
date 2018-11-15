import unittest
from Infrastructure.WebDriverWrapper import Wrapper


class BasicTestClass():
    driver = Wrapper()

    def setUp(self):
        print('init the remote webdriver')
        self.driver.init('http://localhost:4444/wd/hub')

    def tearDown(self):
        print('test ended')
        print('**************************************')


