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

        MainScreen.clickOnPaymentMethods()
        MainScreen.clickOnAddNewCard()
        MainScreen.enterCcNumber("4111-1111-1111-1111")
        MainScreen.enterExpDate("12/18")
        MainScreen.enterCvc('123')
        MainScreen.enterPostalCode('12333')
        MainScreen.ClickOnCcSubmit()
        MainScreen.closeWallet()
"""
        FormPage.enterEmail('galgal12345@gmail.com')
        FormPage.submitEmail()
        FormPage.enterFullName("gal tester")
        FormPage.enterPin(1234)
        FormPage.enterDate("01/02/2003")
        FormPage.chooseOptinTrue()
        FormPage.submitForm()
"""

if __name__ == "__main__":
    unittest.main()
