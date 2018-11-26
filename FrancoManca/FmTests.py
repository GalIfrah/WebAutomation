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

        Wallet.clickOnPaymentMethods()
        Wallet.clickOnAddNewCard()
        Wallet.enterCcNumber()
        Wallet.enterExpDate()
        Wallet.enterCvc()
        Wallet.enterPostalCode()
        Wallet.ClickOnCcSubmit()
        Wallet.closeWallet()
"""
        EnterEmailPage.enterEmail('galgal12345@gmail.com')
        EnterEmailPage.submitEmail()
        FormPage.enterFullName("gal tester")
        FormPage.enterPin(1234)
        FormPage.enterDate("01/02/2003")
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
"""

if __name__ == "__main__":
    unittest.main()
