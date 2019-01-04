import unittest

from selenium.common.exceptions import NoSuchElementException

from Infrastructure.BasicTest import BasicTestClass
from App import PageObjects
from App.PageObjects import *



class Tests(BasicTestClass, unittest.TestCase):

    def test_100_footerText(self):

        HomePage.openSut()

        Connect.login()

        HomePage.startOrder2()


class ConnectTests(BasicTestClass, unittest.TestCase):

    def test_100_registration(self):

        HomePage.openSut()

        Connect.register()

        currentLoginButtonText = HomePage.getLoginButtonText()

        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, currentLoginButtonText)


    def test_101_login(self):

        # login
        Connect.login()

        currentLoginButtonText = HomePage.getLoginButtonText()

        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, currentLoginButtonText)

        # logout
        Connect.logout()

        currentLoginButtonText = HomePage.getLoginButtonText()

        self.assertTrue(currentLoginButtonText == beforeLoginButtonText, currentLoginButtonText)

    def test_102_checkMigration(self):
        pass


class HomeScreenTests(BasicTestClass, unittest.TestCase):

    def test_100_openSut(self):

        HomePage.openSut()

        currentAppLink = HomePage.getSutUrl()

        if env == 'test':

            expectedAppUrl = params['SUT']['TEST']

        elif env == 'prod':

            expectedAppUrl = params['SUT']['PROD']


        self.assertEqual(currentAppLink, expectedAppUrl, 'URLS_NOT_EQUALS' + "   " + currentAppLink)


    @unittest.skipIf(PageObjects.params['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'] == 0,
                     reason="FEATURE_NOT_EXIST")
    def test_101_checkBusinessLink(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        currentAppLinkText = HomePage.getAppLinkText()

        expectedAppLinkText = params['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']

        self.assertEqual(currentAppLinkText, expectedAppLinkText, 'not match')

    def test_102_getInputsPlaceHolders(self):

        HomePage.openSut()

        inputsPlaceHolders = HomePage.getInputsPlaceHolder()

        self.assertEqual(inputsPlaceHolders[0], params['HOME_PAGE']['TEXTS']['SELECT_LOCATION_PLACE_HOLDER_TEXT'],
                         'LOCATION_PLACE_HOLDERS_NOT_EQUALS')
        self.assertEqual(inputsPlaceHolders[1], params['HOME_PAGE']['TEXTS']['SELECT_DATE_PLACE_HOLDER_TEXT'],
                         'DATE_PLACE_HOLDERS_NOT_EQUALS')
        self.assertEqual(inputsPlaceHolders[2], params['HOME_PAGE']['TEXTS']['SELECT_TIME_PLACE_HOLDER_TEXT'],
                         'TIME_PLACE_HOLDERS_NOT_EQUALS')

    def test_103_CheckInputsWithData(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        HomePage.chooseLocation()

        GenericPO.webDriver.saveScreenShot(1)

    def test_104_clickOnConnect(self):

        HomePage.openSut()

        GenericPO.webDriver.saveScreenShot(1)

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        self.assertTrue(EnterPhonePage.getPhoneFieldElement().is_displayed(), "true")

    def test_105_footerText(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        CurrentFooterText = HomePage.getFooterTxt()[0]

        expectedFooterText = params['HOME_PAGE']['TEXTS']['FOOTER_FIRST_PART_TEXT']

        self.assertEqual(CurrentFooterText, expectedFooterText, 'not match')


class WalletTests(BasicTestClass, unittest.TestCase):

    def test_100_openWallet(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        walletSection = GenericPO.webDriver.waitForVisibilityOfElem(params['WALLET']['LOCATORS']['CARDS_SECTION'])

        self.assertIsNotNone(walletSection)

    def test_101_addPaymentMethod_first(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # add first card
        Wallet.addCreditCard()

        numberOfCards = Wallet.getUserCardsNumber()

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            self.assertEqual(numberOfCards, 1, 'not all cards added... missing ' + str(1 - numberOfCards) + "cards")

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0:
            self.assertEqual(numberOfCards, 1, 'not all cards added... missing ' + str(1 - numberOfCards) + "cards")


    def test_102_getUserPayments(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # validation for card
        currentDefaultCardText = Wallet.getUserCardsList()[0].text

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            currentDefaultCardText = Wallet.getUserCardsList()[1].text

        expectedDefaultCardText = params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']

        self.assertEqual(currentDefaultCardText, expectedDefaultCardText, 'CURRENT: ' + currentDefaultCardText +
                         ' EXPECTED: ' + expectedDefaultCardText)



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
                self.fail('DEFAULT_CARD_V_MARK element not found')


        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and numberOfCards[0].text != \
                params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']:

            try:
                defaultCardVmark = Wallet.getUserCardsList()[0].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException:
                self.fail('DEFAULT_CARD_V_MARK element not found')

        else:
            print('USER_HAS_NO_CARDS')

        self.assertIsNotNone(defaultCardVmark, "CARD_ISN'T_DEFAULT")


    def test_104_deleteCard(self):

        HomePage.openSut()

        HomePage.connect()

        Wallet.addCreditCard()

        numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)
        numOfCardsAfterDelete = Wallet.getUserCardsNumber()

        self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')

        # add validation for success popup text & view

    def test_105_CheckInputsValidation(self):
        pass

    def test_106_checkUnsupportedCard(self):
        pass

    def test_107_openWalletFromCheckout(self):
        pass

    def test_108_checkWalletHeader(self):
        pass

    def test_109_checkWeAcceptText(self):
        pass

    def test_110_checkSupportedCards(self):
        pass

    def test_111_checkFooterText(self):
        pass

    def test_112_checkAddCardInputsTexts(self):
        pass

    def test_113_checkCancelApplyButtonsText(self):
        pass



"""
class Tests(BasicTestClass, unittest.TestCase):

     def test_100_enterAndDeleteCard(self):

        HomePage.openSut()
        
        HomePage.connect()

        Wallet.addCreditCard()

        numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)
        numOfCardsAfterDelete = Wallet.getUserCardsNumber()

        self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')


class FlowTests(BasicTestClass, unittest.TestCase):

    def test_100_sanity(self):

        HomePage.openSut()
        GenericPO.webDriver.saveScreenShot(1)

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()
        GenericPO.webDriver.saveScreenShot(2)

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()
        GenericPO.webDriver.saveScreenShot(3)

        EnterEmailPage.enterUnExistEmail()
        EnterEmailPage.submitEmail()

        FormPage.enterFullName()
        FormPage.enterPin()
        FormPage.enterDate()
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
        GenericPO.webDriver.saveScreenShot(4)

        Account.clickOnPaymentMethods()
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        GenericPO.webDriver.saveScreenShot(5)

        Wallet.ClickOnCcSubmit()
        GenericPO.webDriver.saveScreenShot(6)
        Wallet.closeWallet()

        GenericPO.webDriver.saveScreenShot(7)
        HomePage.chooseLocation()
        GenericPO.webDriver.saveScreenShot(8)
        HomePage.startOrder()
        GenericPO.webDriver.saveScreenShot(9)

        Menu.chooseFirstCategory()
        Menu.chooseFirstItem()
        Menu.clickOnProceedToCheckout()
        GenericPO.webDriver.saveScreenShot(10)


        Checkout.clickOnSubmitOrder()
        GenericPO.webDriver.saveScreenShot(11)
        Checkout.enter4DigitsCode()
        GenericPO.webDriver.saveScreenShot(12)


        Checkout.submit4digitsCode()

        if Checkout.getErrorPopup() is not None:

            text = Checkout.getErrorPopup().text

            GenericPO.webDriver.saveScreenShot(13)

            self.fail("CHECKOUT_ERROR: " + text)

        confirmationText = params['CHECKOUT_SCREEN']['TEXTS']['CONFIRMATION_TEXT']

        self.assertEqual(ConfirmationScreen.getConfirmationText(),
             confirmationText, "actual text is: " + ConfirmationScreen.getConfirmationText() +
                         " and expected is: " + confirmationText)


 



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
"""

