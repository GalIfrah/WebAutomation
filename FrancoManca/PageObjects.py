import json

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
FORM_EMAIL_FIELD = ''
FORM_FULL_NAME_FIELD = '//div[@class="col-12"]/input[@placeholder="Full Name"]'
FORM_PIN_FIELD = '//div[@class="relative-wrapper"]/input[@placeholder="Choose your own 4 digit passcode"]'
FORM_DATE_FIELD = '//div[@class="relative-wrapper"]/input[@placeholder="Date Of Birth"]'
FORM_OPTIN_TRUE = '/html/body/div[1]/div/div/div/div/div[2]/div/ng-include/div/div/form/div[5]/div/label'
FORM_SUBMIT_BUTTON = '//div[@class="continue-btn item-input-disable ng-binding"]'
# python run-tests.py --config=/config/apps/franco.json


class FmHomePage(GenericPO):

    @staticmethod
    def printConfig():
        print(json.dumps(params, indent=4))

    @staticmethod
    def openLoginPage():
        GenericPO.webDriver.openSut(params['SUT']['test'])

    @staticmethod
    def clickOnCookPolicyBtn():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['COOKIES_POLICY_BTN'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromHeader():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['BACK_TO_APP_HEADER'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromLogo():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['BACK_TO_APP_LOGO'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnConnect():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['CONNECT_BTN'], LocatorsType=LocatorsTypes.XPATH).click()


# end of login page class


# login page constants

class EnterPhonePage(GenericPO):

    @staticmethod
    def enterValidPhoneNumber():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], LocatorsType=
                            LocatorsTypes.XPATH).send_keys(params['ENTER_PHONE_PAGE']['DATA']['VALID_PHONE_NUMBER'])

    @staticmethod
    def clickOnSubmitBtn():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_BUTTON'], LocatorsType=
                            LocatorsTypes.XPATH).click()

    @staticmethod
    def enterSmsCode():
        print("enter sms code")
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

    @staticmethod
    def enterFullName(name):
        GenericPO.webDriver.findElementBy(FORM_FULL_NAME_FIELD, LocatorsType=LocatorsTypes.XPATH).send_keys(name)

    @staticmethod
    def enterPin(pin):
        GenericPO.webDriver.findElementBy(FORM_PIN_FIELD, LocatorsType=LocatorsTypes.XPATH).send_keys(pin)

    @staticmethod
    def enterDate(date):
        GenericPO.webDriver.findElementBy(FORM_DATE_FIELD, LocatorsType=LocatorsTypes.XPATH).send_keys(date)

    @staticmethod
    def chooseOptinTrue():
        GenericPO.webDriver.findElementBy(FORM_OPTIN_TRUE, LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def submitForm():
        GenericPO.webDriver.findElementBy(FORM_SUBMIT_BUTTON, LocatorsType=LocatorsTypes.XPATH).click()
# end of enter phone class

# class EnterEmailPage(GenericPO):
