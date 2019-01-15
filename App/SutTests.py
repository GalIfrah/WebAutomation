import unittest
from App import PageObjects
from App.PageObjects import *
from Utils.ErrorHandler import ErrorsHandler



class Tests(BasicTestClass, unittest.TestCase):


    def test_100_checkAgeRestriction(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseSecondCategory()

        self.assertTrue(
           GenericPO.webDriver.remoteWebDriver.find_element_by_xpath("//*[@id='store-cg-title'']/div[2]/nav/ul/li[2][@class='category-item ng-scope active']" is not None
                                                                     )

        )


class ConnectTests(BasicTestClass, unittest.TestCase):

    def test_100_registration(self):

        HomePage.openSut()

        Connect.register()

        currentLoginButtonText = HomePage.getLoginButtonText()

        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, ErrorsHandler.LOGIN_ERROR[1] + " " +
                        currentLoginButtonText)


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

    def test_102_wrongSmsCode(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.enterWrongSmsCode()

        EnterPhonePage.submitSmsCode()

        wrongSmsPopUp = EnterPhonePage.getPopup()

        self.assertIsNotNone(wrongSmsPopUp, ErrorsHandler.MISSING_POPUP)

        popupText = EnterPhonePage.getPopupText()

        self.assertEqual(popupText, params['ENTER_PHONE_PAGE']['TEXTS']['WRONG_SMS_POPUP_TEXT'], ErrorsHandler.WRONG_POPUP_TEXT)

    def test_103_resendCode(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()

        EnterPhonePage.submitPhoneNumber()

        EnterPhonePage.clickOnResendCode()

        resendSmsPopUp = EnterPhonePage.getPopup()

        self.assertIsNotNone(resendSmsPopUp, ErrorsHandler.MISSING_POPUP)

        resendSmsPopUpText = EnterPhonePage.getPopupText()

        self.assertEqual(resendSmsPopUpText, params['ENTER_PHONE_PAGE']['TEXTS']['RESEND_CODE_POPUP_TEXT'], ErrorsHandler.WRONG_POPUP_TEXT)

        # add ok clicking & enter the new code with the wrong sms before

    def test_104_checkMigration(self):
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

    def test_104_checkLocationList(self):

        HomePage.openSut()

        Connect.login()

        locationsList = HomePage.getLocationsList()

        expectedLocationNumber = 0

        for location in locationsList:

            self.assertEqual(location.text, params['HOME_PAGE']['DATA']['FULL_LOCATIONS_NAMES'][expectedLocationNumber])

            expectedLocationNumber += 1

    def test_104_connectButton(self):

        HomePage.openSut()

        GenericPO.webDriver.saveScreenShot(1)

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        self.assertTrue(EnterPhonePage.getPhoneFieldElement().is_displayed(), ErrorsHandler.ELEMENT_NOT_VISIBLE)

    def test_105_footerText(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        CurrentFooterText = HomePage.getFooterTxt()[0]

        expectedFooterText = params['HOME_PAGE']['TEXTS']['FOOTER_FIRST_PART_TEXT']

        self.assertEqual(CurrentFooterText, expectedFooterText, ErrorsHandler.TEXT_IS_WRONG)


class WalletTests(BasicTestClass, unittest.TestCase):

    def test_100_openWallet(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        walletSection = GenericPO.webDriver.waitForVisibilityOfElem(params['WALLET']['LOCATORS']['CARDS_SECTION'])

        self.assertIsNotNone(walletSection, ErrorsHandler.ELEMENT_IS_NONE)

    def test_101_addPaymentMethod_first(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # add first card
        Wallet.addCreditCard()

        numberOfCards = Wallet.getUserCardsNumber()

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            self.assertEqual(numberOfCards, 1, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS)

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0:
            self.assertEqual(numberOfCards, 1, str(1 - numberOfCards) + ErrorsHandler.MISSING_CARDS)

    def test_102_getUserPayments(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        # validation for card
        currentDefaultCardText = Wallet.getUserCardsList()[0].text

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] == 0:
            currentDefaultCardText = Wallet.getUserCardsList()[1].text

        expectedDefaultCardText = params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']

        self.assertEqual(currentDefaultCardText, expectedDefaultCardText, ErrorsHandler.TEXT_IS_WRONG + " " + expectedDefaultCardText)

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

        if params['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and numberOfCards[0].text != \
                params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']:

            try:
                defaultCardVmark = Wallet.getUserCardsList()[0].find_element_by_xpath(params['WALLET']['LOCATORS']
                                                                                      ['DEFAULT_CARD_V_MARK'])
            except NoSuchElementException:
                self.fail(ErrorsHandler.ELEMENT_NOT_VISIBLE)

        else:
            print('USER_HAS_NO_CARDS')

        self.assertIsNotNone(defaultCardVmark, ErrorsHandler.CARD_IS_NOT_DEFAULT)


    def test_104_CheckInputsValidation(self):
        # ask for value attributes
        pass

    def test_105_checkUnsupportedCard(self):
        pass

    def test_106_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        Wallet.clickOnCcCancelButton()

        self.assertFalse(Wallet.clickOnCcCancelButton(), "CANCEL_BUTTON_ISN'T_CLICKED")

    def test_107_checkCancelApplyButtonsText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        Wallet.clickOnAddNewCard()

        applyButtonText = Wallet.getCcApplyButtonText()

        self.assertEqual(applyButtonText, params['WALLET']['TEXTS']['APPLY_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

        cancelButtonText = Wallet.getCcCancelButtonText()

        self.assertEqual(cancelButtonText, params['WALLET']['TEXTS']['CANCEL_BUTTON_TEXT'], "BUTTON_TEXT_IS_WRONG")

    def test_108_deleteCard(self):

        HomePage.openSut()

        # Connect.login()

        Connect.login()

        Wallet.addCreditCard()

        numOfCardsBeforeDelete = Wallet.getUserCardsNumber()

        Wallet.clickOnDeleteCardButton()

        Wallet.clickOnDeleteYes()

        time.sleep(1)
        numOfCardsAfterDelete = Wallet.getUserCardsNumber()

        self.assertGreater(numOfCardsBeforeDelete, numOfCardsAfterDelete, 'CARD_NOT_DELETED')

        # add validation for success popup text & view

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

        self.assertEqual(weAcceptedCardText, params['WALLET']['TEXTS']['ACCEPTED_CARDS_TEXT'],
                         "WE_ACCEPT_TEXT_IS_WRONG")

    def test_111_checkSupportedCardsImages(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        acceptedCards = GenericPO.webDriver.remoteWebDriver.find_elements_by_xpath(
            params['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])

        acceptedCardsLen = len(acceptedCards)

        self.assertEqual(acceptedCardsLen, 4, ErrorsHandler.MISSING_SUPPORTED_CARDS)

        acceptedCardsUrl = []

        words = ["visa", "amex", "maestro", "mastercard"]

        for card in acceptedCards:
            acceptedCardsUrl.append(card.get_attribute('src'))

        i = 0

        for word in words:
            print(acceptedCardsUrl[i])
            self.assertTrue(word in acceptedCardsUrl[i], 'word not exist')
            i += 1

    def test_112_checkFooterText(self):

        HomePage.openSut()

        Connect.login()

        Account.clickOnPaymentMethods()

        pciFooterText = Wallet.getPciFooterText()

        self.assertEqual(pciFooterText, params['WALLET']['TEXTS']['PCI_FOOTER_TEXT'], ErrorsHandler.TEXT_IS_WRONG)

    def test_113_checkAddCardInputsHeaders(self):
        pass

    def test_114_openWalletFromCheckout(self):
        pass


class WalletTests(BasicTestClass, unittest.TestCase):

    def test_100_chooseFirstCategory(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseFirstCategory()

    @unittest.skipIf(params['MENU']['DATA']['AGE_LIMIT'] == 0, reason="FEATURE_NOT_EXIST")
    def test_101_checkAgeRestriction(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseRestrictedAgeCategory()

        popupHeaderText = Menu.getPopupHeaderText()

        self.assertEqual(popupHeaderText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_HEADER_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        popupBodyText = Menu.getPopupText()

        self.assertEqual(popupBodyText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_BODY_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        Menu.clickOnPopupOkBtn()

        self.assertTrue(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath(
            '//a/dl/dt[text()="No Logo Pale Ale"]').is_displayed(), ErrorsHandler.ELEMENT_NOT_VISIBLE)

    @unittest.skipIf(params['MENU']['DATA']['AMOUNT_LIMIT'] == 0, reason="FEATURE_NOT_EXIST")
    def test_102_checkOrderItemLimit(self):

        Connect.login()

        HomePage.startOrder(1)

        for i in range(params['MENU']['DATA']['AMOUNT_LIMIT'] + 1):
          Menu.chooseSecondItem()

        moreThenSixText = Menu.getPopupText()

        self.assertEqual(moreThenSixText, params['MENU']['TEXTS']['MORE_THEN_6_POP_UP_TEXT'], ErrorsHandler.TEXT_IS_WRONG)