from SutTests.TestsClassesInit import *


class ConnectTestsClass(BasicTestClass, unittest.TestCase):

    def test_100_registration(self):

        HomePage.openSut()

        Connect.register()

        currentLoginButtonText = HomePage.getLoginButtonText()

        beforeLoginButtonText = params['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']

        self.assertTrue(currentLoginButtonText != beforeLoginButtonText, ErrorsHandler.LOGIN_ERROR + " " +
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



    def test_104_checkMigration(self):
        pass
