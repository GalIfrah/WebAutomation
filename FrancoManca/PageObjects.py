import json
from builtins import print
from selenium.common.exceptions import StaleElementReferenceException
from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes
import time
import unittest

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

ACCOUNT_BUTTON = '//ul[@id="profile-menu"]'
PERSONAL_INFO_BUTTON = '//li[@class="profile-item ng-binding ng-scope account-info"]'


PAYMENT_METHODS_BUTTON = '//ul/li[@class="profile-item ng-binding ng-scope payment-methods"]'



CC_VALUES_IFRAME = '//*[@id="myc-wallet-modal-outer"]/div[1]/div[2]/div[1]/div[1]/iframe'
ADD_NEW_CARD_BUTTON = '//div[@class="myc-wallet-inner myc-wallet-payment-modal"]/div[2]/div[1]/div[2]/ul/li[' \
                      '@class="add-new-card"] '
CC_NUMBER_INPUT = 'creditNumber'
EXP_DATE_INPUT = 'fullYear'
CVC_INPUT = 'cvc'
POSTCODE_INPUT = 'postalCode'
SUBMIT_CC_BUTTON = 'submit'
WALLET_X_BUTTON = '//*[@id="myc-wallet-modal-outer"]/div[1]/div[3]'

# python run-tests.py --config=/config/apps/franco.json


class HomePage(GenericPO):

    @staticmethod
    def openLoginPage():
        params['ENTER_EMAIL_PAGE']['DATA']['UN_EXIST_EMAIL'] = "GAL"
        print(params['ENTER_EMAIL_PAGE']['DATA']['UN_EXIST_EMAIL'])
        GenericPO.webDriver.openSut(params['SUT']['test'])

    @staticmethod
    def clickOnCookPolicyBtn():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['COOKIES_POLICY_BTN'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromHeader():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['BACK_TO_APP_HEADER'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def backToFmFromLogo():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['BACK_TO_APP_LOGO'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnConnect():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['CONNECT_BTN'],
                                          LocatorsType=LocatorsTypes.XPATH).click()
        GenericPO.webDriver.saveScreenShot()

# end of login page class


# login page constants

class EnterPhonePage(GenericPO):

    @staticmethod
    def enterValidPhoneNumber():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], LocatorsType=
        LocatorsTypes.XPATH).send_keys(params['ENTER_PHONE_PAGE']['DATA']['VALID_PHONE_NUMBER'])
        GenericPO.webDriver.saveScreenShot()

    @staticmethod
    def clickOnSubmitBtn():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_BUTTON'], LocatorsType=
        LocatorsTypes.XPATH).click()

    @staticmethod
    def enterSmsCode():
        print("enter sms code")
        code = input()
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE'], LocatorsType=LocatorsTypes.XPATH).send_keys(code)

    @staticmethod
    def submitSmsCode():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_SMS_CODE'], LocatorsType=LocatorsTypes.XPATH).click()


class EnterEmailPage(GenericPO):

    @staticmethod
    def enterEmail():
        UN_EXIST_EMAIL = GenericPO.webDriver.createRandomMail()
        GenericPO.webDriver.findElementBy(params['ENTER_EMAIL_PAGE']['LOCATORS']['ENTER_EMAIL_FIELD'], LocatorsType=LocatorsTypes.XPATH).send_keys(UN_EXIST_EMAIL)

    @staticmethod
    def submitEmail():
        GenericPO.webDriver.findElementBy(params['ENTER_EMAIL_PAGE']['LOCATORS']['SUBMIT_EMAIL_BUTTON'], LocatorsType=LocatorsTypes.XPATH).click()


class FormPage(GenericPO):

    @staticmethod
    def enterFullName():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_FULL_NAME_FIELD'], LocatorsType=LocatorsTypes.XPATH).send_keys(params['FORM_PAGE']['DATA']['NAME'])

    @staticmethod
    def enterPin():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_PIN_FIELD'], LocatorsType=LocatorsTypes.XPATH).send_keys(params['FORM_PAGE']['DATA']['PIN'])

    @staticmethod
    def enterDate():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_DATE_FIELD'], LocatorsType=LocatorsTypes.XPATH).send_keys(params['FORM_PAGE']['DATA']['DATE'])

    @staticmethod
    def chooseOptinTrue():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_OPTIN_TRUE'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def submitForm():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_SUBMIT_BUTTON'], LocatorsType=LocatorsTypes.XPATH).click()


class Wallet(GenericPO):

    @staticmethod
    def clickOnPaymentMethods():
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['ACCOUNT']['ACCOUNT_BUTTON'], params['HOME_PAGE']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])

    @staticmethod
    def clickOnAddNewCard():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['ACCOUNT']['ADD_NEW_CARD_BUTTON'], LocatorsType=LocatorsTypes.XPATH).click()
        # time.sleep(4)
        # move the frame switching to here

    @staticmethod
    def enterCcNumber():
        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CC_NUMBER_INPUT'], LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['VALID_CC_NUMBER'])

        except StaleElementReferenceException:
            print('stale element')

    @staticmethod
    def enterExpDate():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['EXP_DATE_INPUT'], LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['EXP_DATE'])

    @staticmethod
    def enterCvc():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CVC_INPUT'], LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['CVC'])

    @staticmethod
    def enterPostalCode():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['POSTCODE_INPUT'], LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['POSTCODE'])

    @staticmethod
    def ClickOnCcSubmit():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['SUBMIT_CC_BUTTON'], LocatorsType=LocatorsTypes.ID).click()
        GenericPO.webDriver.remoteWebDriver.switch_to.default_content()
        time.sleep(5)

    @staticmethod
    def closeWallet():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['WALLET_X_BUTTON'], LocatorsType=LocatorsTypes.XPATH).click()



# end of enter phone class

# class EnterEmailPage(GenericPO):
