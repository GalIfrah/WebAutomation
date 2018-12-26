import sys
from multiprocessing import TimeoutError

import logger
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


class Wrapper:
    remoteWebDriver = None

    def initDesktop(self, remote_url):
        urllib3.disable_warnings(urllib3.exceptions)

        desired_caps = {'platform': 'WINDOWS', 'browserName': 'chrome'}

        self.remoteWebDriver = webdriver.Remote(remote_url, desired_caps)

        self.remoteWebDriver.maximize_window()


    def initMobile(self, remote_url, device_model):

        urllib3.disable_warnings(urllib3.exceptions)

        mobile_emulation = {"deviceName": device_model}

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.remoteWebDriver = webdriver.Remote(command_executor=remote_url,
                              desired_capabilities=chrome_options.to_capabilities())


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
            logger.error('time out error')

        except NoSuchElementException as E:
            logger.error(self, 'element not found')

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


    def selectFromDropDown(self, drop_down_locator, option_text):
        selector = Select(self.remoteWebDriver.find_element_by_id(drop_down_locator))
        selector.select_by_visible_text(option_text)



    def waitForElemToBeClickable(self, elementLocator):
        for x in range(5):
            try:
                self.remoteWebDriver.find_element_by_xpath(elementLocator).click()
                break

            except Exception:
                print("not found yet")
                time.sleep(1)


    def waitForElemToBeDisplayed(self, elementLocator):

        self.displayed = False

        for x in range(5):
            try:
                if self.remoteWebDriver.find_element_by_xpath(elementLocator).is_displayed() is True:
                    self.displayed = True
                    break

            except Exception:
                print("not displayed yet")
                time.sleep(1)
# remove waiting for next time
        return self.displayed

    def waitForInvisibilityOfElem(self, elementLocator):
            element = WebDriverWait(self.remoteWebDriver, 5).until(
                ec.invisibility_of_element_located((By.XPATH, elementLocator)))

            return element

    def waitForVisibilityOfElem(self, elementLocator):
            try:
                element = WebDriverWait(self.remoteWebDriver, 10).until(
                 ec.visibility_of_element_located((By.XPATH, elementLocator)))
                return element

            except TimeoutException:
                print("there is no popup")






    def switchToIframe(self, element):
        self.remoteWebDriver.switch_to.frame(element)


    def getCurrentUrl(self):
        currentUrl = self.remoteWebDriver.current_url

        return currentUrl


    def refreshPage(self):
        self.remoteWebDriver.refresh()


    def saveScreenShot(self, i):
        time.sleep(1)

        TestsName.test_name = sys._getframe(1).f_code.co_name


        if i == 0:
            filename = TestsName.test_name + '_screenShot.png'
            self.remoteWebDriver.save_screenshot(
                'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\ScreenShots/' + filename)

        elif i != 0:
            filename = TestsName.test_name + '_screenShot' + str(i) + '.png'
            self.remoteWebDriver.save_screenshot(
                'C:\\Users\galif\PycharmProjects\WebAutomation\Reports\ScreenShots' + filename)

        return TestsName.test_name






