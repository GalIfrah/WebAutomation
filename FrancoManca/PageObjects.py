from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes

params = GenericPO.webDriver.loadJson()

# login page constants
SUT = "https://order.francomanca.co.uk/"
COOKIES_POLICY_BTN = "//div[@class='continue ng-binding']"
BACK_TO_FM_HEADER = "//div[@class='back-to-site-msg ng-binding']/a[@href='http://www.francomanca.co.uk/']"
BACK_TO_FM_LOGO = "//a[@ng-if='homeUrl']"
CONNECT_BTN = '//*[@id="login-btn"]/span'

PHONE_FIELD = '//input[@name="phone"]'
SUBMIT_BUTTON = '/html/body/div[1]/div/div/div/div/div[2]/div/ng-include/div/div[2]/form/div[1]/div[2]'
ENTER_SMS_CODE = '//form/div/div/input'
SUBMIT_SMS_CODE = '//form/div/div/div'
ENTER_EMAIL_FIELD = '//input[@type="email"]'
SUBMIT_EMAIL_BUTTON = '//div[@type="button"]'


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
        GenericPO.webDriver.findElementBy(CONNECT_BTN, LocatorsType=LocatorsTypes.XPATH).click()


# end of login page class


# login page constants

class EnterPhonePage(GenericPO):

    @staticmethod
    def enterValidPhoneNumber(phone):
        GenericPO.webDriver.findElementBy(PHONE_FIELD, LocatorsType=LocatorsTypes.XPATH).send_keys(phone)

    @staticmethod
    def clickOnSubmitBtn():
        GenericPO.webDriver.findElementBy(SUBMIT_BUTTON, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def enterSmsCode():
        print "enter sms code"
        code = input()
        GenericPO.webDriver.findElementBy(ENTER_SMS_CODE, LocatorsType=LocatorsTypes.XPATH).send_keys(code)

    @staticmethod
    def submitSmsCode():
        GenericPO.webDriver.findElementBy(SUBMIT_SMS_CODE, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def enterEmail(email):
        GenericPO.webDriver.findElementBy(ENTER_EMAIL_FIELD, LocatorsType=LocatorsTypes.XPATH).send_keys(email)

    @staticmethod
    def submitEmail():
        GenericPO.webDriver.findElementBy(SUBMIT_EMAIL_BUTTON, LocatorsType=LocatorsTypes.XPATH).click()

# end of enter phone class

# class EnterEmailPage(GenericPO):
