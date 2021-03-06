import traceback

from pip._vendor.distlib.compat import raw_input
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.by import By

from Infrastructure.GenericPageObject import GenericPO
from Infrastructure.Locators import LocatorsTypes
from Infrastructure.BasicTest import BasicTestClass
from Services.ErrorService import ErrorsHandler
from Services.utils import ProjectUtils
import time
import logging
from Infrastructure.BasicTest import *
from Services.SmsServices import *

params = None
env = ''
reporterType = ''


class Connect(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def register():

        Connect.login()

        EnterEmailPage.enterUnExistEmail()

        EnterEmailPage.submitEmail()

        FormPage.enterFullName()

        FormPage.enterPin()

        FormPage.enterDate()

        FormPage.chooseOptinTrue()

        FormPage.submitForm()

    @staticmethod
    def login():

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber(phoneNumber=SmsService.getFirstAvailableNumber())

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.enterSmsCode()

        EnterPhonePage.submitSmsCode()

    @staticmethod
    def logout():

        Account.clickOnLogOut()

        Account.logOutYes()


class HomePage(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def openSut():

        if env == 'test':
            GenericPO.webDriver.openSut(params['SUT']['TEST'])

        if env == 'prod':
            GenericPO.webDriver.openSut(params['SUT']['PROD'])

    @staticmethod
    def getSutUrl():
        text = GenericPO.webDriver.getCurrentUrl()

        return text

    @staticmethod
    def clickOnCookPolicyBtn():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getCookPolicyTxt():
        txt = GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                                LocatorsType=LocatorsTypes.XPATH).text
        return txt

    @staticmethod
    def goToAppSite_header():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getAppLinkText():
        appLinkText = GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                                        LocatorsType=LocatorsTypes.XPATH).text
        return appLinkText

    @staticmethod
    def clickOnConnect():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['CONNECT_BTN'],
                                          LocatorsType=LocatorsTypes.ID).click()

    @staticmethod
    def getLoginButtonText():
        time.sleep(3)
        text = GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def getInputsPlaceHolder():
        placeHolders = [
            GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_PLACE_HOLDER'],
                                              LocatorsType=LocatorsTypes.XPATH).text,
            GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['SELECT_DATE_PLACE_HOLDER'],
                                              LocatorsType=LocatorsTypes.XPATH).text,
            GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['SELECT_TIME_PLACE_HOLDER'],
                                              LocatorsType=LocatorsTypes.XPATH).text]
        return placeHolders

    @staticmethod
    def chooseLocation():
        GenericPO.webDriver.selectFromDropDown(params['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                               params['HOME_PAGE']['DATA']['SECOND_LOCATION'])

        time.sleep(2)

    @staticmethod
    def getLocationsList():
        locationsList = GenericPO.webDriver.getDropDownOptionsList(params['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'])

        return locationsList

    @staticmethod
    def chooseDate():
        GenericPO.webDriver.selectFromDropDown(params['HOME_PAGE']['LOCATORS']['SELECT_DATE_DROP_DOWN'],
                                               params['HOME_PAGE']['DATA']['TOMORROW'])

    @staticmethod
    def chooseTime():
        GenericPO.webDriver.selectFromDropDown(params['HOME_PAGE']['LOCATORS']['SELECT_TIME_DROP_DOWN'],

                                               params['HOME_PAGE']['DATA']['TIME'])

    @staticmethod
    def startOrder(testLocationNumber):
        if testLocationNumber == 1:
                GenericPO.webDriver.selectFromDropDown(params['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                               params['HOME_PAGE']['DATA']['FIRST_LOCATION_NOT_WORKING'])

        if testLocationNumber == 2:
                time.sleep(1)
                GenericPO.webDriver.selectFromDropDown(params['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                                   params['HOME_PAGE']['DATA']['SECOND_LOCATION'])


        time.sleep(2)
        GenericPO.webDriver.waitForElemToBeClickable(params['HOME_PAGE']['LOCATORS']['START_ORDER_BUTTON'])

        time.sleep(3)
        if GenericPO.webDriver.getCurrentUrl() == params['MENU']['LOCATORS']['MENU_URL']:
                    pass


        elif HomePage.getStartOrderPopup() is not None:

                if HomePage.getStartOrderPopup().text == params['HOME_PAGE']['TEXTS']['START_ORDER_CHOOSE_LOCATION_POPUP_TEXT']:

                        HomePage.clickOnStartOrderPopupButton()

                        HomePage.chooseLocation()

                        HomePage.startOrder(1)

                elif HomePage.getStartOrderPopup().text == params['HOME_PAGE']['TEXTS']['START_ORDER_TIME_EXCEEDED_POPUP_TEXT']:

                        HomePage.clickOnStartOrderPopupButton()

                        HomePage.startOrder(2)

                elif HomePage.getStartOrderPopup().text == params['HOME_PAGE']['TEXTS']['START_ORDER_NOT_ACCEPTING_POPUP_TEXT']:

                        HomePage.clickOnStartOrderPopupButton()

                        HomePage.startOrder(2)

                elif HomePage.getStartOrderPopup().text == params['HOME_PAGE']['TEXTS']['START_ORDER_SELECT_TIME_POPUP_TEXT']:

                        HomePage.clickOnStartOrderPopupButton()

                        HomePage.chooseLocation()

                        HomePage.startOrder(2)




    @staticmethod
    def getStartOrderPopup():
        element = GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_TEXT_AREA'],
                                      LocatorsType=LocatorsTypes.XPATH)
        return element

    @staticmethod
    def clickOnStartOrderPopupButton():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnTermsAndConditions():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['TERMS_AND_COND_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def ClIckOnPrivacyPolicy():
        GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['PRIVACY_POLICY'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getFooterTxt():

        footerTxts = [GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['FOOTER_FIRST_PART'],
                                                        LocatorsType=LocatorsTypes.XPATH).text,
                      GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['FOOTER_SECOND_PART'],
                                                        LocatorsType=LocatorsTypes.XPATH).text,
                      GenericPO.webDriver.findElementBy(params['HOME_PAGE']['LOCATORS']['FOOTER_THIRD_PART'],
                                                        LocatorsType=LocatorsTypes.XPATH).text]
        return footerTxts



class Account(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def clickOnAccountInformation():
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PERSONAL_INFO_BUTTON'])

    @staticmethod
    def clickOnPaymentMethods():
        time.sleep(3)
        # GenericPO.webDriver.waitForVisibilityOfElem(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])

        try:

             GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                               params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
             time.sleep(1)

             walletSection = GenericPO.webDriver.waitForVisibilityOfElem(params['WALLET']['LOCATORS']['CARDS_SECTION'])


             if walletSection is None:

                 GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                                  params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
                 time.sleep(1)

        except NoSuchElementException:
            logging.error(ErrorsHandler.WALLET_IS_NOT_VISIBLE)

    @staticmethod
    def clickOnGiftCards():
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          params['HOME_PAGE']['LOCATORS']['ACCOUNT']['GIFT_CARDS'])

    @staticmethod
    def clickOnHistory():
        time.sleep(2)
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          params['HOME_PAGE']['LOCATORS']['ACCOUNT']['HISTORY'])
        time.sleep(2)


    @staticmethod
    def clickOnLogOut():
        GenericPO.webDriver.hoverAndClick(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                          params['HOME_PAGE']['LOCATORS']['ACCOUNT']['LOG_OUT'])

    @staticmethod
    def logOutYes():
        GenericPO.webDriver.findElementBy(params['LOGOUT_SCREEN']['YES_BTN'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def logOutNo():
        GenericPO.webDriver.findElementBy(params['LOGOUT_SCREEN']['NO_BTN']).click()



class AccountInformation(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def getNameText():
        text = GenericPO.webDriver.findElementBy("//*[@id='modal-body']/div/div[1]/div/input",
                                            LocatorsType=LocatorsTypes.XPATH).text
        return text



class History(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def getHistoryList():

        historyList = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(params['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'],
                                            LocatorsType=LocatorsTypes.XPATH)
        return historyList


    @staticmethod
    def getHistoryFirstOrderPrice():

        historyList = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(
                                params['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'])

        firstOrderPrice = historyList[0].find_element_by_xpath(params['HISTORY_SCREEN']['LOCATORS']['FIRST_ORDER_PRICE']).text

        return firstOrderPrice



class EnterPhonePage(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def getPhoneFieldElement():
        element = GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], LocatorsType=
        LocatorsTypes.XPATH)
        return element

    @staticmethod
    def enterValidPhoneNumber(phoneNumber):
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], LocatorsType=
                                    LocatorsTypes.XPATH).send_keys(phoneNumber)

    @staticmethod
    def submitPhoneNumber():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_BUTTON'], LocatorsType=
                                        LocatorsTypes.XPATH).click()

        GenericPO.webDriver.switchToWindow(1)

    @staticmethod
    def getPopup():
        screenPopup = GenericPO.webDriver.waitForVisibilityOfElem(
            params['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP'])

        return screenPopup

    @staticmethod
    def getPopupText():
        screenPopupText = GenericPO.webDriver.waitForVisibilityOfElem(
            params['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screenPopupText

    @staticmethod
    def clickOnPopupOkBtn():
        GenericPO.webDriver.waitForVisibilityOfElem(
            params['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_OK']).click

    @staticmethod
    def enterSmsCode():

        code = SmsService.getSmsCode()

        GenericPO.webDriver.switchToWindow(0)

        time.sleep(1)

        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(code)

        # code = ApiHelper.getCode(phoneToken)
        # code = raw_input()

    @staticmethod
    def enterWrongSmsCode():

        randSmsCode = ProjectUtils.createRandomSmsCode()

        GenericPO.webDriver.waitForVisibilityOfElem(params['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE']).send_keys(randSmsCode)

    @staticmethod
    def submitSmsCode():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_SMS_CODE'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

        GenericPO.webDriver.waitForVisibilityOfElem(params['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])

        #time.sleep(3)

    @staticmethod
    def clickOnResendCode():
        GenericPO.webDriver.findElementBy(params['ENTER_PHONE_PAGE']['LOCATORS']['RESEND_CODE'],
                                          LocatorsType=LocatorsTypes.XPATH).click()


class EnterEmailPage(GenericPO):

    def __init__(self):
        pass

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

    def __init__(self):
        pass

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

        GenericPO.webDriver.waitForVisibilityOfElem(params['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])
        # time.sleep(3)




class Wallet(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def clickOnAddNewCard():
        if len(Wallet.getUserCardsList()) >= 1 and Wallet.getUserCardsList()[0].text == params['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and Wallet.getUserCardsList()[0].text != params['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

    @staticmethod
    def getWalletHeader():
        walletHeader = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['WALLET_HEADER'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return walletHeader

    @staticmethod
    def enterCcNumber():
        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CC_NUMBER_INPUT'],
                                              LocatorsType=LocatorsTypes.ID).send_keys(
                params['WALLET']['DATA']['FIRST_CARD_DETAILS']['VALID_CC_NUMBER'])

        except StaleElementReferenceException:
            print('stale element')

    @staticmethod
    def enterExpDate():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['EXP_DATE_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['FIRST_CARD_DETAILS']['EXP_DATE'])

    @staticmethod
    def enterCvc():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CVC_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['FIRST_CARD_DETAILS']['CVC'])

    @staticmethod
    def enterPostalCode():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['POSTCODE_INPUT'],
                                          LocatorsType=LocatorsTypes.ID).send_keys(params['WALLET']['DATA']['FIRST_CARD_DETAILS']['POSTCODE'])

    @staticmethod
    def clickOnCcApplyButton():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                          LocatorsType=LocatorsTypes.ID).click()
        GenericPO.webDriver.remoteWebDriver.switch_to.default_content()

        time.sleep(6)

    @staticmethod
    def getCcApplyButtonText():
        GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                           (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        applyButtonText = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                          LocatorsType=LocatorsTypes.ID).text
        return applyButtonText

    @staticmethod
    def clickOnCcCancelButton():


        try:
            GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                               (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                          LocatorsType=LocatorsTypes.ID).click()
            GenericPO.webDriver.remoteWebDriver.switch_to.default_content()

        except WebDriverException:
            return False

    @staticmethod
    def getCcCancelButtonText():
        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        cancelButtonText = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                                            LocatorsType=LocatorsTypes.ID).text
        return cancelButtonText

    @staticmethod
    def getUserCardsList():

        cardListElement = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CARDS_SECTION'],
            LocatorsType=LocatorsTypes.XPATH)

        cards = cardListElement.find_elements_by_tag_name(params['WALLET']['LOCATORS']['USER_CARDS'])

        return cards

    @staticmethod
    def getUserCardsNumber():

        cardListElement = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['CARDS_SECTION'],
            LocatorsType=LocatorsTypes.XPATH)

        cards = cardListElement.find_elements_by_tag_name(params['WALLET']['LOCATORS']['USER_CARDS'])

        if cards[0].text == params['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

            del cards[0:1]

        return len(cards)

    @staticmethod
    def clickOnDeleteCardButton():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getDeletePopupText():
        text = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_POPUP'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def clickOnDeleteYes():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getDeleteYesButtonText():
        text = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def clickOnDeleteNo():
        GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getDeleteNoButtonText():
        text = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                                 LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def getDefaultCardVmark():
        element = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['DEFAULT_CARD_V_MARK'],
                                          LocatorsType=LocatorsTypes.XPATH)
        return element

    @staticmethod
    def getWeAcceptCardsText():
        weAcceptCardsText = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['ACCEPTED_CARDS_TEXT_AREA'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return weAcceptCardsText

    @staticmethod
    def getWeAcceptCardsIcons():
        GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(params['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])

    @staticmethod
    def getPciFooterText():
        pciFooterText = GenericPO.webDriver.findElementBy(params['WALLET']['LOCATORS']['PCI_FOOTER_TEXT_AREA'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return pciFooterText

    @staticmethod
    def getWalletModal():
        walletModal = GenericPO.webDriver.waitForVisibilityOfElem(params['WALLET']['LOCATORS']['CARDS_SECTION'])

        return walletModal

    @staticmethod
    def closeWallet():
        GenericPO.webDriver.waitForElemToBeClickable(params['WALLET']['LOCATORS']['WALLET_X_BUTTON'])

    @staticmethod
    def addCreditCard():

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.enterCcNumber()

        Wallet.enterExpDate()

        Wallet.enterCvc()

        Wallet.enterPostalCode()

        Wallet.clickOnCcApplyButton()


    @staticmethod
    def addCreditCardFromCheckout():

        Wallet.clickOnAddNewCard()

        Wallet.enterCcNumber()

        Wallet.enterExpDate()

        Wallet.enterCvc()

        Wallet.enterPostalCode()

        Wallet.clickOnCcApplyButton()


class Menu(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def chooseFirstCategory():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['FIRST_CATEGORY'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def chooseSecondCategory():
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['SECOND_CATEGORY'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def checkIfCategoryChosen():
        isChosen = False

        if GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['SECOND_CATEGORY_ACTIVE'], LocatorsType=LocatorsTypes.XPATH) is not None:
            isChosen = True

        return isChosen

    @staticmethod
    def chooseRestrictedAgeCategory():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(params['MENU']['DATA']['AGE_RESTRICTED_CATEGORY'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def chooseUpSaleItem():
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['UP_SALE_ITEM'], LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def firstCategoryText():
        text = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['FIRST_CATEGORY'], LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def chooseSecondItem():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['SECOND_ITEM'],
                                          LocatorsType=LocatorsTypes.XPATH).click()


    @staticmethod
    def clickOnMenuToast():
        if BasicTestClass.platform == 'mobile':
            time.sleep(1)
            GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MENU_TOAST'],
                                              LocatorsType=LocatorsTypes.XPATH).click()
            time.sleep(1)

    @staticmethod
    def getSecondItemText():
        text = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['SECOND_ITEM'],
                                                 LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def getCartSecondItemText():
        text = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['CART_SECOND_ITEM_TEXT'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return text

    @staticmethod
    def getTotalPrice():

        price = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['CART_TOTAL'],
                                                  LocatorsType=LocatorsTypes.XPATH).text

        return price

    @staticmethod
    def clickOnEditItem():
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['EDIT_ITEM_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def clickOnEditItemFromCart():
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['EDIT_ITEM_FROM_CART'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getModifiersModal():
        modifierModal = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MODIFIER_MODAL'],
                                                       LocatorsType=LocatorsTypes.XPATH)
        return modifierModal

    @staticmethod
    def getModifiersModalHeaderText():
        headerText = GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MODIFIER_MODAL_HEADER'],
                                          LocatorsType=LocatorsTypes.XPATH).text
        return headerText

    @staticmethod
    def closeModifiersWindow():
        time.sleep(1)
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['CLOSE_MODIFIER_X_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def deleteItemFromCart():
        GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['DELETE_ITEM_FROM_CART'],
                                          LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getCartItemsList():
        cartItemsList = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(params['MENU']['LOCATORS']['CART_ITEMS_CONTAINER'])

        return cartItemsList

    @staticmethod
    def getModifiersBySection():
        time.sleep(1)

        modifiersList = GenericPO.webDriver.remoteWebDriver.find_elements(by=By.XPATH, value=params['MENU']['LOCATORS']['SECOND_CATEGORY_MODIFIERS'])

        return modifiersList

    @staticmethod
    def checkModifierActivity(element):
        isActive = False

        if element.find_element_by_xpath(params['MENU']['LOCATORS']['ACTIVE_MODIFIER']) is not None:
            isActive = True

        return isActive

    @staticmethod
    def moveToCart():

        if BasicTestClass.platform == 'mobile':
            time.sleep(1)
            GenericPO.webDriver.findElementBy("//div[@id='toast-container']",
                                              LocatorsType=LocatorsTypes.XPATH).click()
            time.sleep(1)

            GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MOBILE_CART_ICON'],
                                              LocatorsType=LocatorsTypes.XPATH).click()


    @staticmethod
    def clickOnProceedToCheckout():

        #if BasicTestClass.platform == "desktop":

                GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['PROCEED_TO_CHECKOUT_BUTTON'],
                                              LocatorsType=LocatorsTypes.XPATH).click()

        #elif BasicTestClass.platform == "mobile":

                # GenericPO.webDriver.findElementBy("//div[@id='toast-container']",
                #                                   LocatorsType=LocatorsTypes.XPATH).click()
                # time.sleep(1)
                #
                # GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MOBILE_CART_ICON'],
                #                                   LocatorsType=LocatorsTypes.XPATH).click()

                # GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['PROCEED_TO_CHECKOUT_BUTTON'],
                #                               LocatorsType=LocatorsTypes.XPATH).click()

    @staticmethod
    def getPopup():
        screenPopup = GenericPO.webDriver.waitForVisibilityOfElem(
            params['MENU']['LOCATORS']['SCREEN_POPUP'])

        return screenPopup

    @staticmethod
    def getPopupHeaderText():
        screenPopupHeaderText = GenericPO.webDriver.waitForVisibilityOfElem(
            params['MENU']['LOCATORS']['SCREEN_POPUP_HEADER']).text

        return screenPopupHeaderText

    @staticmethod
    def getPopupText():
        screenPopupText = GenericPO.webDriver.waitForVisibilityOfElem(
            params['MENU']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screenPopupText

    @staticmethod
    def getUpSalePopupText():
        upSalePopupText = GenericPO.webDriver.waitForVisibilityOfElem(
            params['MENU']['LOCATORS']['UP_SALE_POPUP_BODY']).text

        return upSalePopupText

    @staticmethod
    def clickOnPopupOkBtn():
        GenericPO.webDriver.findElementBy(
            params['MENU']['LOCATORS']['SCREEN_POPUP_OK'], LocatorsType=LocatorsTypes.XPATH).click()


class Checkout(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def addPaymentFromCheckout():
        GenericPO.webDriver.findElementBy("//div[@class='add-payment-method ng-binding ng-scope']",
                                          LocatorsType=LocatorsTypes.XPATH)

    @staticmethod
    def clickOnSubmitOrder():
        if GenericPO.webDriver.waitForInvisibilityOfElem("//div[@class='loading']") is True:
                GenericPO.webDriver.waitForElemToBeClickable(params['CHECKOUT_SCREEN']['LOCATORS']['SUBMIT_ORDER_BUTTON'])


    @staticmethod
    def enter4DigitsCode():
        GenericPO.webDriver.findElementBy(params['CHECKOUT_SCREEN']['LOCATORS']['ENTER_PIN_INPUT'],
                                          LocatorsType=LocatorsTypes.XPATH).send_keys(
            params['FORM_PAGE']['DATA']['PIN'])

    @staticmethod
    def submit4digitsCode():
        GenericPO.webDriver.findElementBy(params['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'],
                                          LocatorsType=LocatorsTypes.XPATH).click()
        time.sleep(2)

    @staticmethod
    def Pass4DigitsPin():
       if params['CHECKOUT_SCREEN']['DATA']['4_DIGIT_EXIST'] == 1:

        Checkout.enter4DigitsCode()

        Checkout.submit4digitsCode()

       else:
           pass

    @staticmethod
    def getErrorPopup():
        popUpElement = GenericPO.webDriver.waitForVisibilityOfElem(params['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP'])
        return popUpElement

    @staticmethod
    def clickOnPopUpOkBtn():
        GenericPO.webDriver.findElementBy(params['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'], LocatorsType=LocatorsTypes.XPATH).click()
        time.sleep(1)

    @staticmethod
    def getErrorPopupText():
        text = GenericPO.webDriver.waitForVisibilityOfElem(params['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP']).text

        return text

    @staticmethod
    def clickOnManagePaymentMethod():
        GenericPO.webDriver.findElementBy(params['CHECKOUT_SCREEN']['LOCATORS']['MANAGE_PAYMENT_METHOD'], LocatorsType=LocatorsTypes.XPATH).click()



class ConfirmationScreen(GenericPO):

    def __init__(self):
        pass

    @staticmethod
    def getConfirmationText():
        try:
            element = GenericPO.webDriver.findElementBy(params['CONFIRMATION_SCREEN']['LOCATORS']['CONFIRMATION_TEXT_AREA'],
                                                                 LocatorsType=LocatorsTypes.XPATH)

            return element.text

        except AttributeError:
            logging.error(ErrorsHandler.CONFIRMATION_MISSING)


    @staticmethod
    def clickOnDone():
        GenericPO.webDriver.findElementBy(params['CONFIRMATION_SCREEN']['LOCATORS']['DONE_BUTTON'],
                                          LocatorsType=LocatorsTypes.XPATH).click()
        time.sleep(4)
        # remove the sleep

    @staticmethod
    def getTotalPrice():
        price = GenericPO.webDriver.findElementBy(params['CONFIRMATION_SCREEN']['LOCATORS']['TOTAL'],
                                                  LocatorsType=LocatorsTypes.XPATH).text

        return price


