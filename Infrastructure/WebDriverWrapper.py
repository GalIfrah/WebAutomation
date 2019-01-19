import sys
from multiprocessing import TimeoutError
import logging
from selenium import webdriver
import urllib3
from selenium.webdriver.common.action_chains import ActionChains
import time
from Infrastructure.Locators import LocatorsTypes
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)
from selenium.webdriver.support.ui import Select
from Utils.TestName import TestsName
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from Utils.ErrorHandler import ErrorsHandler

class Wrapper:

    remoteWebDriver = None

    def initDesktop(self, remote_url):
        urllib3.disable_warnings(urllib3.exceptions)

        desired_caps = {'platform': 'WINDOWS', 'browserName': 'chrome'}

        self.remoteWebDriver = webdriver.Remote(remote_url, desired_caps)

        self.remoteWebDriver.maximize_window()



    def initMobile(self, remote_url, device_model):

        urllib3.disable_warnings(urllib3.exceptions)

        #mobile_emulation = {"deviceName": device_model}

        #chrome_options = webdriver.ChromeOptions()

        #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)



        #mobile_emulation = {

         #   "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

          #  "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

        # chrome_options = Options()

        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


       # self.remoteWebDriver = webdriver.Remote(command_executor=remote_url,
                              #desired_capabilities=chrome_options.to_capabilities())
        urllib3.disable_warnings(urllib3.exceptions)

        desired_caps = {'platform': 'WINDOWS', 'browserName': 'chrome'}

        self.remoteWebDriver = webdriver.Remote(remote_url, desired_caps)
        self.remoteWebDriver.set_window_size(260, 800)

    def openSut(self, url):
        self.remoteWebDriver.get(url)


    def closeCurrent(self):
        self.remoteWebDriver.close()


    def closeAll(self):
        self.remoteWebDriver.quit()


    def findElementBy(self, value, LocatorsType):

        elementAssigned = False

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

            elementAssigned = True

        except TimeoutError as E:
            logging.error(ErrorsHandler.TIMEOUT_ERROR)

        except NoSuchElementException as E:
            logging.error(ErrorsHandler.NO_SUCH_ELEMENT)

        except UnboundLocalError as E:
            E.with_traceback(E.__context__)

        if elementAssigned is True:
            return element
        else:
            print(ErrorsHandler.ELEMENT_NOT_ASSIGNED_YET)


    def hoverAndClick(self, firstElementLocator, secondElementLocator):

        action = ActionChains(self.remoteWebDriver)

        action.move_to_element(self.remoteWebDriver.find_element_by_xpath(firstElementLocator)).move_to_element(
            (self.remoteWebDriver.find_element_by_xpath(secondElementLocator))).double_click((
             self.remoteWebDriver.find_element_by_xpath(secondElementLocator))).perform()


    def selectFromDropDown(self, drop_down_locator, option_text):
        time.sleep(1)
        selector = Select(self.remoteWebDriver.find_element_by_id(drop_down_locator))
        selector.select_by_visible_text(option_text)


    def getDropDownOptionsList(self, drop_down_locator):
        selector = Select(self.remoteWebDriver.find_element_by_id(drop_down_locator))

        return selector.options


    def waitForElemToBeClickable(self, elementLocator):

        try:
            WebDriverWait(self.remoteWebDriver, 10).until(
                ec.element_to_be_clickable((By.XPATH, elementLocator))).click()

        except TimeoutException:
            print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)


    def waitForInvisibilityOfElem(self, elementLocator):
            isVisible = WebDriverWait(self.remoteWebDriver, 5).until(
                ec.invisibility_of_element_located((By.XPATH, elementLocator)))

            return isVisible


    def waitForVisibilityOfElem(self, elementLocator):
            try:
                element = WebDriverWait(self.remoteWebDriver, 7).until(
                 ec.visibility_of_element_located((By.XPATH, elementLocator)))
                return element

            except TimeoutException:
                print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)


    def switchToIframe(self, element):
        self.remoteWebDriver.switch_to.frame(element)


    def getCurrentUrl(self):
        currentUrl = self.remoteWebDriver.current_url

        return currentUrl


    def refreshPage(self):
        self.remoteWebDriver.refresh()


    def saveScreenShot(self, i, testName):
        time.sleep(1)

        filename = testName + '_screenShot.png'

        if i == 0:

            self.remoteWebDriver.save_screenshot(
                'C:\\Users\MyCheck\PycharmProjects\WebAutomation\Reports\ScreenShots\\' + filename)

        elif i != 0:

            self.remoteWebDriver.save_screenshot(
                'C:\\Users\MyCheck\PycharmProjects\WebAutomation\Reports\ScreenShots\\' + filename)

        return testName
