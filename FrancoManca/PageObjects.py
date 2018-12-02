from builtins import print
from selenium.common.exceptions import StaleElementReferenceException
from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes
from Utils.utils import ProjectUtils
import time

params = ProjectUtils.loadJson()


class HomePage(GenericPO):

    @staticmethod
    def openSut():
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

    @staticmethod
    def chooseLocation():
        GenericPO.webDriver.selectFromDropDown('home-select-location', 'AireusTest')

    @staticmethod
    def startOrder():
        GenericPO.webDriver.waitForElemToBeClickable(params['HOME_PAGE']['START_ORDER_BUTTON'])
        time.sleep(1)

        for x in range(5):
            try:
                if GenericPO.webDriver.getCurrentUrl() == params['MENU']['MENU_URL']:
                    print('')
                    break
                elif GenericPO.webDriver.findElementBy(params['HOME_PAGE']['START_ORDER_POPUP_TEXT'],
                                                       LocatorsType=LocatorsTypes.XPATH).is_displayed():

                    GenericPO.webDriver.findElementBy(params['HOME_PAGE']['START_ORDER_POPUP_BUTTON'],
                                                      LocatorsType=LocatorsTypes.XPATH).click()

                    GenericPO.webDriver.selectFromDropDown('home-select-location', 'fm2')

                    GenericPO.webDriver.waitForElemToBeClickable(params['HOME_PAGE']['START_ORDER_BUTTON'])

                    break

            except Exception:
                print("still not found the url/popup")
                time.sleep(1)


class Account(GenericPO):

    @staticmethod
    def clickOnAccountInformation():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['BACK_TO_APP_LOGO'],
                                          LocatorsType=LocatorsTypes.XPATH).click()


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
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(code)

    @staticmethod
    def submitSmsCode():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_SMS_CODE'],
                                          LocatorsType=LocatorsTypes.XPATH).click()
        time.sleep(2)


class EnterEmailPage(GenericPO):

    @staticmethod
    def enterUnExistEmail():
        UN_EXIST_EMAIL = ProjectUtils.createRandomMail()
        GenericPO.webDriver.findElementBy(params['ENTER_EMAIL_PAGE']['LOCATORS']['ENTER_EMAIL_FIELD'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(UN_EXIST_EMAIL)

    @staticmethod
    def submitEmail():
        GenericPO.webDriver.findElementBy(params['ENTER_EMAIL_PAGE']['LOCATORS']['SUBMIT_EMAIL_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()


class FormPage(GenericPO):

    @staticmethod
    def enterFullName():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_FULL_NAME_FIELD'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(
            params['FORM_PAGE']['DATA']['NAME'])

    @staticmethod
    def enterPin():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_PIN_FIELD'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(
            params['FORM_PAGE']['DATA']['PIN'])

    @staticmethod
    def enterDate():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_DATE_FIELD'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(
            params['FORM_PAGE']['DATA']['DATE'])

    @staticmethod
    def chooseOptinTrue():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_OPTIN_TRUE'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def submitForm():
        GenericPO.webDriver.findElementBy(params['FORM_PAGE']['LOCATORS']['FORM_SUBMIT_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()


class Wallet(GenericPO):

    @staticmethod
    def clickOnPaymentMethods():
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          params['HOME_PAGE']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])

    @staticmethod
    def clickOnAddNewCard():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def enterCcNumber():
        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CC_NUMBER_INPUT'],
                                              LocatorsType=LocatorsTypes.ID).send_keys(
                params['WALLET']['DATA']['VALID_CC_NUMBER'])

        except StaleElementReferenceException:
            print('stale element')

    @staticmethod
    def enterExpDate():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['EXP_DATE_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['EXP_DATE'])

    @staticmethod
    def enterCvc():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CVC_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['CVC'])

    @staticmethod
    def enterPostalCode():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['POSTCODE_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['POSTCODE'])

    @staticmethod
    def ClickOnCcSubmit():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['SUBMIT_CC_BUTTON'],
                                          LocatorsType=LocatorsTypes.ID).click()
        GenericPO.webDriver.remoteWebDriver.switch_to.default_content()
        time.sleep(5)

    @staticmethod
    def closeWallet():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['WALLET_X_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def ClickOnDeleteCard():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnDeleteYes():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

class Menu(GenericPO):

    @staticmethod
    def chooseFirstItem():
        GenericPO.webDriver.findElementBy(params['MENU']['FIRST_ITEM'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnProceedToCheckout():
        GenericPO.webDriver.findElementBy(params['MENU']['PROCEED_TO_CHECKOUT_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()
        GenericPO.webDriver.waitForElemToBeClickable("//span[@class='ng-binding']")
