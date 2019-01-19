from SutTests.TestsClassesInit import *


class FlowsTestsClass(BasicTestClass, unittest.TestCase):


    def test_100_sanity(self):

            Connect.register()

            Wallet.addCreditCard()

            Wallet.closeWallet()

            HomePage.startOrder(2)

            Menu.chooseSecondItem()

            Menu.clickOnProceedToCheckout()

            if Checkout.getErrorPopup().is_displayed() and Checkout.getErrorPopupText() == params['CHECKOUT_SCREEN']['TEXTS']['EXCEEDED_PICKUP_TIME_TEXT']:
                Checkout.clickOnPopUpOkBtn()

            Checkout.clickOnSubmitOrder()

            Checkout.enter4DigitsCode()

            Checkout.submit4digitsCode()

            confiramtionText = ConfirmationScreen.getConfirmationText()
            self.assertEqual()

    def test_101_walletFlow(self):
        pass

    def test_102_(self):
        pass
