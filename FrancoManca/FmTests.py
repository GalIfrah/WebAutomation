import unittest


from Infrastructure.BasicTest import BasicTestClass
from FrancoManca.PageObjects import *
import HtmlTestRunner

html_report_dir = 'C:/Users/galif/PycharmProjects/WebAutomation/Reports'


class FmTestsClass(BasicTestClass, unittest.TestCase):
    def test_100_OpenFm(self):
        FmHomePage.openLoginPage()
        FmHomePage.clickOnCookPolicyBtn()
        FmHomePage.clickOnConnect()

        EnterPhonePage.enterValidPhoneNumber("+972542567405")
        EnterPhonePage.clickOnSubmitBtn()


if __name__ == "__main__":

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))


