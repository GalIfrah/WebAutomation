from SutTests.TestsClassesInit import *


class EnterPhoneTestsClass:

    def test_100_wrongSmsCode(self):

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


    def test_101_resendCode(self):

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

