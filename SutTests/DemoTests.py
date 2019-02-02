import unittest
from builtins import print
from Utils.BrowserStackService import browserStack

from App import PageObjects
from App.PageObjects import *
from Utils.ErrorHandler import ErrorsHandler
import requests

class DemoTestsClass(BasicTestClass, unittest.TestCase):



    def test_100_addPaymentMethod_first(self):
            
            HomePage.openSut()
            
            Connect.register()
            
            # add first card
            Wallet.addCreditCard()

            numberOfCards = Wallet.getUserCardsNumber()

            try:

                if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
                    self.assertEqual(numberOfCards, 2, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS) # 1

                if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0:
                    self.assertEqual(numberOfCards, 1, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS)

            except AssertionError:

                browserStack.changeTestStatus(self, "Error", ErrorsHandler.MISSING_CARDS)
    """
    
    def test_101_validateDefaultCard(self):

            HomePage.openSut()

            Connect.login()

            Account.clickOnPaymentMethods()

            numberOfCards = Wallet.getUserCardsList()

            defaultCardVmark = None

            if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0 and len(numberOfCards) > 1:

                try:
                    defaultCardVmark = Wallet.getUserCardsList()[1].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                          ['DEFAULT_CARD_V_MARK'])
                except NoSuchElementException:
                    self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

            if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and numberOfCards[0].text == \
                    params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']:

                try:
                    defaultCardVmark = Wallet.getUserCardsList()[0].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                          ['DEFAULT_CARD_V_MARK'])
                except NoSuchElementException:
                    self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

            else:
                print('USER_HAS_NO_CARDS')

            self.assertIsNotNone(defaultCardVmark, ErrorsHandler.CARD_IS_NOT_DEFAULT)


    def test_102_deleteCard(self):

            HomePage.openSut()

            Connect.login()

            Wallet.addCreditCard()

            numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

            Wallet.clickOnDeleteCardButton()

            Wallet.clickOnDeleteYes()

            time.sleep(1)
            numOfCardsAfterDelete = Wallet.getUserCardsNumber()

            self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')
        

    def test_103_sanity(self):

            Connect.login()

            # Wallet.addCreditCard()
            #
            # Wallet.closeWallet()

            HomePage.startOrder(2)

            GenericPO.webDriver.saveScreenShot(1, self.testName)

            Menu.chooseFirstCategory()

            Menu.chooseSecondItem()

            Menu.moveToCart()

            cartTotal = Menu.getTotalPrice()

            Menu.clickOnProceedToCheckout()

            if Checkout.getErrorPopup() is not None:

                   if params['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT'] in Checkout.getErrorPopupText():

                          Checkout.clickOnPopUpOkBtn()

            Checkout.clickOnSubmitOrder()

            Checkout.Pass4DigitsPin()

            confirmationHeaderText = ConfirmationScreen.getConfirmationText()

            self.assertEqual(confirmationHeaderText, params['CONFIRMATION_SCREEN']['TEXTS']['CONFIRMATION_TEXT'])


            confirmationTotalPrice = ConfirmationScreen.getTotalPrice()

            self.assertEqual(cartTotal, confirmationTotalPrice, ErrorsHandler.TOTAL_PRICE_ERROR)

            ConfirmationScreen.clickOnDone()

            GenericPO.webDriver.remoteWebDriver.back()

            Account.clickOnHistory()

            historyOrderPrice = History.getHistoryFirstOrderPrice()

            self.assertEqual(historyOrderPrice, confirmationTotalPrice, ErrorsHandler.WRONG_HISTORY_TOTAL)


    @unittest.skipIf(params['MENU']['DATA']['AGE_LIMIT'] == 0, reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP + ' ' + BasicTestClass.appName)
    def test_104_checkAgeRestriction(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseRestrictedAgeCategory()

        popupHeaderText = Menu.getPopupHeaderText()

        self.assertEqual(popupHeaderText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_HEADER_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        popupBodyText = Menu.getPopupText()

        self.assertEqual(popupBodyText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_BODY_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        Menu.clickOnPopupOkBtn()

        self.assertTrue(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath(
        params['MENU']['DATA']['AGE_PASSING_INDICATOR']).is_displayed(), ErrorsHandler.ELEMENT_NOT_VISIBLE)

        
        
                    def test_100_addPaymentMethod_first(self):
            HomePage.openSut()

            browserStack.changeTestStatus(self, "Error")
    """