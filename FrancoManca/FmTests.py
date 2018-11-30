import unittest

from Infrastructure.BasicTest import BasicTestClass
from FrancoManca.PageObjects import *
import HtmlTestRunner.runner

html_report_dir = 'C:/Users/MyCheck/PycharmProjects/WebAutomation/Reports'


class FmTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_OpenFm(self):

        HomePage.openLoginPage()

        HomePage.clickOnCookPolicyBtn()
        HomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()

        """
        EnterEmailPage.enterEmail()
        EnterEmailPage.submitEmail()

        FormPage.enterFullName()
        FormPage.enterPin()
        FormPage.enterDate()
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
  
        Wallet.clickOnPaymentMethods()
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        Wallet.ClickOnCcSubmit()
        Wallet.closeWallet()
"""
        HomePage.chooseLocation()
        HomePage.startOrder()

        Menu.chooseFirstItem()
        Menu.clickOnProceedToCheckout()



if __name__ == "__main__":
    unittest.main()
