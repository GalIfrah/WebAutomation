from selenium import webdriver
import json
from selenium import webdriver
from Infrastructure.Locators import LocatorsTypes
from selenium.common.exceptions import (InvalidArgumentException, WebDriverException)
from selenium.common.exceptions import (InvalidArgumentException,
                                        NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui



class Wrapper:
    remoteWebDriver = None

    def init(self, remote_url):
        desired_caps = {'platform': 'WINDOWS', 'browserName': 'chrome'}

        self.remoteWebDriver = webdriver.Remote(remote_url, desired_caps)

        self.remoteWebDriver.maximize_window()

    def openSut(self, url):
        self.remoteWebDriver.get(url)

    def closeCurrent(self):
        self.remoteWebDriver.close()

    def closeAll(self):
        self.remoteWebDriver.quit()

    def findElementBy(self, value, LocatorsType=LocatorsTypes):

        if LocatorsType.XPATH:
            self.remoteWebDriver.implicitly_wait(10)
            element = self.remoteWebDriver.find_element_by_xpath(value)
            return element

        if LocatorsType.ID:
            self.remoteWebDriver.implicitly_wait(10)
            element = self.remoteWebDriver.find_element_by_id(value)
            return element

        if LocatorsType.CLASS_NAME:
            self.remoteWebDriver.implicitly_wait(10)
            element = self.remoteWebDriver.find_element_by_class_name(value)
            return element

        if LocatorsType.NAME:
            self.remoteWebDriver.implicitly_wait(10)
            element = self.remoteWebDriver.find_element_by_name(value)
            return element

        if LocatorsType.CSS_SELECTOR:
            self.remoteWebDriver.implicitly_wait(10)
            element = self.remoteWebDriver.find_element_by_css_selector(value)
            return element

        else:
            raise NoSuchElementException()

    def takeScreenShot(self):
        self.remoteWebDriver.get_screenshot_as_png()

    def saveScreenShot(self, ProjectName):

        if ProjectName == "FrancoManca":
            filename = 'fmScreenShot'

        if ProjectName == "TRG":
            filename = 'trgScreenShot'

        self.remoteWebDriver.save_screenshot(filename)

    def loadJson(self):
        with open('C:\\Users\galif\PycharmProjects\WebAutomation\FrancoManca\gal.json', 'r') as f:
            obj = json.load(f)

        return obj

    def waitforele(self, value):
        self.remoteWebDriver.implicitly_wait(10)
