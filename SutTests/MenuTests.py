import unittest
from App import PageObjects
from App.PageObjects import *
from Utils.ErrorHandler import ErrorsHandler


class Menu(BasicTestClass, unittest.TestCase):

    def test_100_chooseFirstCategory(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseFirstCategory()

    @unittest.skipIf(params['MENU']['DATA']['AGE_LIMIT'] == 0, reason="FEATURE_NOT_EXIST")
    def test_101_checkAgeRestriction(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseRestrictedAgeCategory()

        popupHeaderText = Menu.getPopupHeaderText()

        self.assertEqual(popupHeaderText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_HEADER_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        popupBodyText = Menu.getPopupText()

        self.assertEqual(popupBodyText, params['MENU']['TEXTS']['ALCOHOL_RESTRICTION_BODY_TEXT'],
                         ErrorsHandler.TEXT_IS_WRONG)

        Menu.clickOnPopupOkBtn()

        self.assertTrue(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath(
            '//a/dl/dt[text()="No Logo Pale Ale"]').is_displayed(), ErrorsHandler.ELEMENT_NOT_VISIBLE)

    @unittest.skipIf(params['MENU']['DATA']['AMOUNT_LIMIT'] == 0, reason="FEATURE_NOT_EXIST")
    def test_102_checkOrderItemLimit(self):

        Connect.login()

        HomePage.startOrder(1)

        for i in range(params['MENU']['DATA']['AMOUNT_LIMIT'] + 1):
          Menu.chooseSecondItem()

        moreThenSixText = Menu.getPopupText()

        self.assertEqual(moreThenSixText, params['MENU']['TEXTS']['MORE_THEN_6_POP_UP_TEXT'], ErrorsHandler.TEXT_IS_WRONG)

