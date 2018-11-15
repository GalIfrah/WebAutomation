from builtins import print

from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes

params = GenericPO.webDriver.loadJson()
print (params)

# login page constants
SUT = "https://order.francomanca.co.uk/"
COOKIES_POLICY_BTN = "//div[@class='continue ng-binding']"
BACK_TO_FM_HEADER = "//div[@class='back-to-site-msg ng-binding']/a[@href='http://www.francomanca.co.uk/']"
BACK_TO_FM_LOGO = "//a[@ng-if='homeUrl']"
CONNECT_BTN = "login-btn"


class FmHomePage(GenericPO):

    @staticmethod
    def openLoginPage():
        GenericPO.webDriver.openSut(params['SUT']['prod'])

    @staticmethod
    def clickOnCookPolicyBtn():
        GenericPO.webDriver.findElementBy(COOKIES_POLICY_BTN, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromHeader():
        GenericPO.webDriver.findElementBy(BACK_TO_FM_HEADER, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromLogo():
        GenericPO.webDriver.findElementBy(BACK_TO_FM_LOGO, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnConnect():
        GenericPO.webDriver.findElementBy(CONNECT_BTN, LocatorsType=LocatorsTypes.ID).click()


# end of login page class


# login page constants

class EnterPhonePage(GenericPO):

    @staticmethod
    def enterValidPhoneNumber():
        dic = GenericPO.webDriver.loadJson()
        print(dic['SUT']['LOGIN_PAGE'])
# end of enter phone class
