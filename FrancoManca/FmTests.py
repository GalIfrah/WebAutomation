import unittest


from Infrastructure.BasicTest import BasicTestClass
from FrancoManca.PageObjects import *
import HtmlTestRunner.runner

html_report_dir = 'C:/Users/MyCheck/PycharmProjects/WebAutomation/Reports'


class FmTestsClass(BasicTestClass, unittest.TestCase):
    def test_100_OpenFm(self):
        FmHomePage.printConfig()
        FmHomePage.openLoginPage()
        FmHomePage.clickOnCookPolicyBtn()
        FmHomePage.clickOnConnect()
        EnterPhonePage.enterValidPhoneNumber()
        EnterPhonePage.clickOnSubmitBtn()
        EnterPhonePage.enterSmsCode()
        EnterPhonePage.submitSmsCode()
        EnterPhonePage.enterEmail('galgal12345@gmail.com')
        EnterPhonePage.submitEmail()
        EnterPhonePage.enterFullName("gal tester")
        EnterPhonePage.enterPin(1234)
        EnterPhonePage.enterDate("01/02/2003")
        EnterPhonePage.chooseOptinTrue()
        EnterPhonePage.submitForm()


if __name__ == "__main__":

    unittest.main()


