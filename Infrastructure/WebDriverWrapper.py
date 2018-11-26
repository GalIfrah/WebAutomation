import sys
from venv import logger
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from Infrastructure.Locators import LocatorsTypes
from selenium.common.exceptions import (InvalidArgumentException,
                                        NoSuchElementException)
import inspect


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

    def findElementBy(self, value, LocatorsType):
        elementFlag = False
        self.remoteWebDriver.implicitly_wait(10)
        try:
            if LocatorsType == LocatorsTypes.XPATH:
                element = self.remoteWebDriver.find_element_by_xpath(value)

            elif LocatorsType == LocatorsTypes.ID:
                element = self.remoteWebDriver.find_element_by_id(value)

            elif LocatorsType == LocatorsTypes.CLASS_NAME:
                element = self.remoteWebDriver.find_element_by_class_name(value)

            elif LocatorsType == LocatorsTypes.NAME:
                element = self.remoteWebDriver.find_element_by_name(value)

            elif LocatorsType == LocatorsTypes.CSS_SELECTOR:
                element = self.remoteWebDriver.find_element_by_css_selector(value)

            elementFlag = True

        except TimeoutError:
            print('time out error')

        except NoSuchElementException:
            logger.error('element not found')

        except UnboundLocalError:
            logger.error("element not assigned to any value yet")

        if elementFlag is True:
            return element
        else:
            logger.error("element not assigned to any value yet")

    def hoverAndClick(self, firstElementLocator, secondElementLocator):

        ActionChains(self.remoteWebDriver)

        ActionChains(self.remoteWebDriver).move_to_element(self.remoteWebDriver.find_element_by_xpath
                                                           (firstElementLocator)).perform()
        ActionChains(self.remoteWebDriver).move_to_element(self.remoteWebDriver.find_element_by_xpath
                                                           (secondElementLocator)).perform()
        time.sleep(3)
        ActionChains(self.remoteWebDriver).double_click(self.remoteWebDriver.find_element_by_xpath
                                                        (secondElementLocator)).perform()

    def switchToIframe(self, element):
        self.remoteWebDriver.switch_to.frame(element)

    def takeScreenShot(self):
        self.remoteWebDriver.get_screenshot_as_png()

    def saveScreenShot(self):

        currentRunningFuncionName = sys._getframe(1).f_code.co_name
        filename = currentRunningFuncionName + '_screenShot.png'

        self.remoteWebDriver.save_screenshot('C:/Users/galif/PycharmProjects/WebAutomation/Reports/ScreenShots/' + filename)

    def loadJson(self):

        with open('AppConfig.json', 'r') as f:

            obj = json.load(f)

        return obj

    def writeToJson(self, data):
        with open('AppConfig.json', 'w') as outfile:

            json.dump(data, outfile)

    def waitforele(self, value):
        self.remoteWebDriver.implicitly_wait(10)

    def createRandomMail(self):
        randEmail = ''.join(random.choice('0123456789ABCDEF') for i in range(16)) + '@mycheck.co.il'

        return randEmail

