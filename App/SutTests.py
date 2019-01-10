import unittest

from selenium.common.exceptions import NoSuchElementException

from Infrastructure.BasicTest import BasicTestClass
from App import PageObjects
from App.PageObjects import *


class Tests(BasicTestClass, unittest.TestCase):

    def test_100_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.register()

        HomePage.startOrder(1)

        Menu.chooseFirstCategory()

        Menu.chooseSecondItem()

        Menu.clickOnProceedToCheckout()

        Checkout.clickOnSubmitOrder()

        Account.clickOnPaymentMethods()

        pciFooterText = Wallet.getPciFooterText()

        self.assertEqual(pciFooterText, params['WALLET']['TEXTS']['PCI_FOOTER_TEXT'], "PCI_FOOTER_TEXT_IS_WRONG")


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

        # Connect.login()
        
        Connect.register()
        
        Wallet.addCreditCard()

        numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)
        numOfCardsAfterDelete = Wallet.getUserCardsNumber()

        self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')

        # add validation for success popup text & view

    def test_105_CheckInputsValidation(self):
        # ask for value attributes
        pass

    def test_106_checkUnsupportedCard(self):
        pass

    def test_107_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.clickOnCcCancelButton()

        self.assertFalse(Wallet.clickOnCcCancelButton(), "CANCEL_BUTTON_ISN'T_CLICKED")

    def test_108_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        applyButtonText = Wallet.getCcApplyButtonText()

        self.assertEqual(applyButtonText, params['WALLET']['TEXTS']['APPLY_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

        cancelButtonText = Wallet.getCcCancelButtonText()

        self.assertEqual(cancelButtonText, params['WALLET']['TEXTS']['CANCEL_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

    def test_109_checkWalletHeader(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        walletHeader = Wallet.getWalletHeader()

        self.assertEqual(walletHeader, params['WALLET']['TEXTS']['WALLET_HEADER_TEXT'], "WALLET_HEADERS_NOT_EQUALS")

    def test_110_checkWeAcceptText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        weAcceptedCardText = Wallet.getWeAcceptCardsText()

        self.assertEqual(weAcceptedCardText, params['WALLET']['TEXTS']['ACCEPTED_CARDS_TEXT'], "WE_ACCEPT_TEXT_IS_WRONG")

    def test_111_checkSupportedCards(self):
        pass

    def test_112_checkFooterText(self):
        pass

    def test_113_checkAddCardInputsHeaders(self):
        pass

    def test_114_openWalletFromCheckout(self):
        pass
