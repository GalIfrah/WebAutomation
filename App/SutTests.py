import unittest
from Infrastructure.BasicTest import BasicTestClass
from App.PageObjects import *
from Utils.TestName import TestsName
import HtmlTestRunner


class HomeScreenTests(BasicTestClass, unittest.TestCase):

    def test_100_openSut(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        currentAppLinkText = HomePage.getAppLinkText()

        expectedAppLinkText = params['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']

        GenericPO.webDriver.saveScreenShot()

        self.assertEqual(currentAppLinkText, expectedAppLinkText, 'not match')

    def test_100_openSut2(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()

        currentAppLinkText = HomePage.getAppLinkText()

        expectedAppLinkText = params['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']

        self.assertEqual(currentAppLinkText, expectedAppLinkText, 'not match')





class FlowTests(BasicTestClass, unittest.TestCase):

    def test_101_sanity(self):

        HomePage.openSut()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        Wallet.clickOnPaymentMethods()
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        Wallet.ClickOnCcSubmit()
        Wallet.closeWallet()

        HomePage.chooseLocation()
        HomePage.startOrder()
        """

        Menu.chooseFirstItem()
        Menu.clickOnProceedToCheckout()

        Checkout.clickOnSubmitOrder()
        Checkout.enter4DigitsCode()
        EnterEmailPage.enterUnExistEmail()
        EnterEmailPage.submitEmail()

        FormPage.enterFullName()
        FormPage.enterPin()
        FormPage.enterDate()
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
"""


"""
        

        
        
        



        Wallet.clickOnPaymentMethods()
        Wallet.ClickOnDeleteCard()
        Wallet.clickOnDeleteYes()
        Wallet.closeWallet()

        
        
        
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        Wallet.ClickOnCcSubmit()

        

        

        HomePage.chooseLocation()

        Menu.chooseFirstItem()
        Menu.clickOnProceedToCheckout()
        
        EnterEmailPage.enterEmail()
        EnterEmailPage.submitEmail()

        FormPage.enterFullName()
        FormPage.enterPin()
        FormPage.enterDate()
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
        
"""








if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
