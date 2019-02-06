import time
from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes


SMS_PROVIDER_SITE = "http://receive-smss.com/"
PHONE_NUMBER_LOCATOR = "//*[@id='content']/div[1]/div/div/div/div[1]/div[2]/div/h4"
PHONE_NUMBER_BUTTON = "//*[@id='content']/div[1]/div/div/div/div[1]/div[3]/div/a"
SMS_TEXT_LOCATOR_LIST = "//*[@id='content']/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]"


class SmsService(GenericPO):


    def __init__(self):
        pass

    @staticmethod
    def getFirstAvailableNumber():

        GenericPO.webDriver.remoteWebDriver.execute_script("window.open('');")

        GenericPO.webDriver.switchToWindow(1)

        GenericPO.webDriver.openSut(SMS_PROVIDER_SITE)

        phoneNumber = GenericPO.webDriver.findElementBy(PHONE_NUMBER_LOCATOR, LocatorsType=LocatorsTypes.XPATH).text

        GenericPO.webDriver.switchToWindow(0)

        return phoneNumber


    @staticmethod
    def getSmsCode():

        time.sleep(3)

        GenericPO.webDriver.findElementBy(PHONE_NUMBER_BUTTON, LocatorsType=LocatorsTypes.XPATH).click()

        receivedSmsList = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(SMS_TEXT_LOCATOR_LIST)

        receivedSmsText = receivedSmsList[0].text

        smsCode = receivedSmsText[receivedSmsText.index(": ") + 2:receivedSmsText.index(" t")]

        GenericPO.webDriver.switchToWindow(0)

        return smsCode



