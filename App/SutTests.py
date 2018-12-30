import unittest
from Infrastructure.BasicTest import BasicTestClass
from App import PageObjects
from App.PageObjects import *


class Tests(BasicTestClass, unittest.TestCase):

    def test_100_stamTest(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        Account.clickOnPaymentMethods()

        currentDefaultCardText = Wallet.getUserCardsList()[1].text
        expectedDefaultCardText = params['WALLET']['TEXTS']['DEFAULT_CARD_TEXT']
        self.assertEqual(currentDefaultCardText, expectedDefaultCardText, 'CURRENT: ' + currentDefaultCardText +
                         ' EXPECTED: ' + expectedDefaultCardText)




class ConnectTests(BasicTestClass, unittest.TestCase):

    def test_100_registration(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        EnterEmailPage.enterUnExistEmail()
        EnterEmailPage.submitEmail()

        FormPage.enterFullName()
        FormPage.enterPin()
        FormPage.enterDate()
        FormPage.chooseOptinTrue()
        FormPage.submitForm()

        currentLoginButtonText = HomePage.getLoginButtonText()
        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, currentLoginButtonText)


    def test_101_login(self):

        # login
        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        currentLoginButtonText = HomePage.getLoginButtonText()
        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, currentLoginButtonText)

        # logout

        Account.clickOnLogOut()
        Account.logOutYes()

        currentLoginButtonText = HomePage.getLoginButtonText()
        self.assertTrue(currentLoginButtonText == beforeLoginButtonText, currentLoginButtonText)

    def test_102_checkMigration(self):
        pass


class HomeScreenTests(BasicTestClass, unittest.TestCase):

    def test_100_openSut(self):

        HomePage.openSut()

        currentAppLink = HomePage.getSutUrl()

        if env == 'test':

            expectedAppUrl = params['SUT']['test']

        elif env == 'prod':

            expectedAppUrl = params['SUT']['prod']

        self.assertEqual(currentAppLink, expectedAppUrl, 'urls not equals')


    @unittest.skipIf(PageObjects.params['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'] == 0,
                     reason="FEATURE_NOT_EXIST")
    def test_101_checkBusinessLink(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        currentAppLinkText = HomePage.getAppLinkText()

        expectedAppLinkText = params['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']

        GenericPO.webDriver.saveScreenShot(1)

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

    def test_103_getInputsPlaceHolders2(self):

        HomePage.openSut()

        inputsPlaceHolders = HomePage.getInputsPlaceHolder()

        self.assertEqual(inputsPlaceHolders[1], params['HOME_PAGE']['TEXTS']['SELECT_LOCATION_PLACE_HOLDER_TEXT'],
                         'LOCATION_PLACE_HOLDERS_NOT_EQUALS')
        self.assertEqual(inputsPlaceHolders[1], params['HOME_PAGE']['TEXTS']['SELECT_DATE_PLACE_HOLDER_TEXT'],
                         'DATE_PLACE_HOLDERS_NOT_EQUALS')
        self.assertEqual(inputsPlaceHolders[2], params['HOME_PAGE']['TEXTS']['SELECT_TIME_PLACE_HOLDER_TEXT'],
                         'TIME_PLACE_HOLDERS_NOT_EQUALS')

    def test_105_CheckInputsWithData(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        HomePage.chooseLocation()

        GenericPO.webDriver.saveScreenShot(1)

    def test_106_clickOnConnect(self):

        HomePage.openSut()

        GenericPO.webDriver.saveScreenShot(1)

        HomePage.clickOnCookPolicyBtn()

        HomePage.clickOnConnect()

        self.assertTrue(EnterPhonePage.getPhoneFieldElement().is_displayed(), "true")

    def test_107_footerText(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        CurrentFooterText = HomePage.getFooterTxt()[0]

        expectedFooterText = params['HOME_PAGE']['TEXTS']['FOOTER_FIRST_PART_TEXT']

        self.assertEqual(CurrentFooterText, expectedFooterText, 'not match')


class WalletTests(BasicTestClass, unittest.TestCase):

    def test_100_openWallet(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        Account.clickOnPaymentMethods()
        # add validation

    def test_101_addPaymentMethod_first(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        Account.clickOnPaymentMethods()

        # add first card

        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        GenericPO.webDriver.saveScreenShot(5)

        Wallet.ClickOnCcSubmit()

        # add second card

        # add logic for second card credentials
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        GenericPO.webDriver.saveScreenShot(5)

        Wallet.ClickOnCcSubmit()

    def test_103_getUserPayments(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        Account.clickOnPaymentMethods()
        # add validation

    def test_104_validateDefaultCard(self):
        pass

    def test_105_deleteCard(self):
        pass

    def test_106_CheckInputsValidation(self):
        pass

    def test_107_checkUnsupportedCard(self):
        pass

    def test_108_openWalletFromCheckout(self):
        pass


"""
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

