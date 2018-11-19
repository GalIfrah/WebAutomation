import unittest


from Infrastructure.BasicTest import BasicTestClass
from FrancoManca.PageObjects import *
import HtmlTestRunner.runner

html_report_dir = 'C:/Users/MyCheck/PycharmProjects/WebAutomation/Reports'


class FmTestsClass(BasicTestClass, unittest.TestCase):
    def test_100_OpenFm(self):
        FmHomePage.openLoginPage()
        FmHomePage.clickOnCookPolicyBtn()
        FmHomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber("+972542567405")
        EnterPhonePage.clickOnSubmitBtn()


if __name__ == "__main__":

    unittest.main()


