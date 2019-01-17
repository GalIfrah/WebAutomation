from TestsClassesInit import *


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




    def test_104_checkMigration(self):
        pass
