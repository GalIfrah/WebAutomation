# from SutTests.TestsClassesInit import *
import unittest
from App import PageObjects
from App.PageObjects import *
from Utils.ErrorHandler import ErrorsHandler



class BetaTestsClass(BasicTestClass, unittest.TestCase):

    def test_103_validateDefaultCard(self):

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

        """
    def test_100_edit_deleteItemFromCart(self):

        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        cartItemsNumberBeforeDelete = len(Menu.getCartItemsList())

        # assert cart items list size before & after deleting the item
        self.assertTrue(cartItemsNumberBeforeDelete == 1, ErrorsHandler.CART_EMPTY)

        Menu.deleteItemFromCart()

        cartItemsNumberAfterADelete = len(Menu.getCartItemsList())

        self.assertTrue(cartItemsNumberAfterADelete == 0, ErrorsHandler.CART_DOES_NOT_EMPTY)


        HomePage.openSut()

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        # Menu.clickOnEditItem()

        list = Menu.getCartItemsList()

        sizeBefore = len(list)

        #Menu.closeModifiersWindow()

        Menu.deleteItemFromCart()

        list = Menu.getCartItemsList()

        sizeAfter = len(list)

        self.assertGreater(sizeBefore, sizeAfter, "sada")




    def test_100_Sanity(self):

        Connect.register()

        Wallet.addCreditCard()

        Wallet.closeWallet()

        HomePage.startOrder(2)

        Menu.chooseSecondItem()

        Menu.clickOnProceedToCheckout()

        if Checkout.getErrorPopup().is_displayed() and Checkout.getErrorPopupText() == params['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT']:
            Checkout.clickOnPopUpOkBtn()

        Checkout.clickOnSubmitOrder()

        Checkout.enter4DigitsCode()

        Checkout.submit4digitsCode()

        confirmationText = ConfirmationScreen.getConfirmationText()

        self.assertEqual(confirmationText, params['CONFIRMATION_SCREEN']['TEXTS']['CONFIRMATION_TEXT'], ErrorsHandler.TEXT_IS_WRONG)
        """