# from SutTests.TestsClassesInit import *
import unittest
from builtins import print

from App import PageObjects
from App.PageObjects import *
from Utils.ErrorHandler import ErrorsHandler


class FlowsTestsClass(BasicTestClass, unittest.TestCase):
    testName = BasicTestClass.testName


    def test_100_sanity(self):

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

