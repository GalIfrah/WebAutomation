import sys
from selenium.webdriver.support import expected_conditions as EC
from venv import logger
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Infrastructure.Locators import LocatorsTypes
from selenium.common.exceptions import (NoSuchElementException)
from selenium.webdriver.support.ui import Select


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

        action = ActionChains(self.remoteWebDriver)

        action.move_to_element(self.remoteWebDriver.find_element_by_xpath(firstElementLocator)).move_to_element(
            (self.remoteWebDriver.find_element_by_xpath(secondElementLocator))).double_click((
            self.remoteWebDriver.find_element_by_xpath(secondElementLocator))).perform()

    # ActionChains(self.remoteWebDriver).move_to_element(self.remoteWebDriver.find_element_by_xpath
    #                                                   (secondElementLocator)).perform()
    #  WebDriverWait(self.remoteWebDriver, 900).until(
    #     EC.element_to_be_clickable((By.XPATH, secondElementLocator)))

    # ActionChains(self.remoteWebDriver).double_click(self.remoteWebDriver.find_element_by_xpath
    #                                               (secondElementLocator)).perform()

    def selectFromDropDown(self, drop_down_locator, option_text):
        selector = Select(self.remoteWebDriver.find_element_by_id(drop_down_locator))
        selector.select_by_visible_text(option_text)

        time.sleep(1)

    def waitForElemToBeClickable(self, elementLocator):
        WebDriverWait(self.remoteWebDriver, 20).until(
            EC.element_to_be_clickable((By.XPATH, elementLocator)))

    def switchToIframe(self, element):
        self.remoteWebDriver.switch_to.frame(element)

    def saveScreenShot(self):

        currentRunningFuncionName = sys._getframe(1).f_code.co_name

        filename = currentRunningFuncionName + '_screenShot.png'

        self.remoteWebDriver.save_screenshot(
            'C:/Users/galif/PycharmProjects/WebAutomation/Reports/ScreenShots/' + filename)

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

# python run-tests.py --config=/config/apps/franco.json
