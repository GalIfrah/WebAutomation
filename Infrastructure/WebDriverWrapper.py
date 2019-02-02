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



    def initMobile(self, remote_url, device_model = False):

        urllib3.disable_warnings(urllib3.exceptions)

        # run on cloud
        desired_cap = {
                        'os_version' : '7.0',
                        'device' : 'Samsung Galaxy S8',
                        'real_mobile' : 'true',
                        'browserstack.local' : 'false'

        }


        self.remoteWebDriver = webdriver.Remote(
            command_executor=remote_url,
            desired_capabilities=desired_cap)

    # run locally

        # mobile_emulation = {"deviceName": "Nexus 5"}
        #
        # chrome_options = webdriver.ChromeOptions()
        #
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        #
        # self.remoteWebDriver = webdriver.Remote(remote_url, desired_capabilities = chrome_options.to_capabilities())


    def openSut(self, url):
        self.remoteWebDriver.get(url)

    def closeCurrent(self):
        self.remoteWebDriver.quit()


    def closeAll(self):
        self.remoteWebDriver.quit()


    def findElementBy(self, value, LocatorsType):

        elementAssigned = False

        try:
            if LocatorsType == LocatorsTypes.XPATH:

                element = WebDriverWait(self.remoteWebDriver, 15).until(
                    ec.visibility_of_element_located((By.XPATH, value)))

            elif LocatorsType == LocatorsTypes.ID:

                element = WebDriverWait(self.remoteWebDriver, 15).until(
                   ec.visibility_of_element_located((By.ID, value)))

            if element is not None:
                elementAssigned = True

        except TimeoutException as E:
            logging.error(ErrorsHandler.TIMEOUT_ERROR)

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

        if i == 0:

            filename = testName + '_screenShot.png'

            self.remoteWebDriver.save_screenshot(

                'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\screenShots\\' + filename)

        elif i != 0:

            filename = testName + '_screenShot' + str(i) + '.png'

            self.remoteWebDriver.save_screenshot(

                'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\screenShots\\' + filename)

        return testName




        # urllib3.disable_warnings(urllib3.exceptions)
        #
        # desired_caps = {'platform': 'WINDOWS', 'browserName': 'chrome'}
        #
        # self.remoteWebDriver = webdriver.Remote(remote_url, desired_caps)
        # self.remoteWebDriver.set_window_size(260, 800)
