from builtins import print

from FrancoManca.PageObjects import SUT
from Infrastructure.GenericPageObject import GenericPO

# login page constants
SUT_Login = 'https://order.therealgreek.com/'


class LoginPage(GenericPO):

    @staticmethod
    def openLoginPage():
        GenericPO.webDriver.openSut(SUT_Login)


# end of login page class


# login page constants
SUT_Phone = 'https://www.python-course.eu/python3_inheritance.php'


class EnterPhonePage(GenericPO):

    @staticmethod
    def enterValidPhoneNumber():
        dic = GenericPO.webDriver.loadJson()
        print(dic['SUT']['LOGIN_PAGE'])
# end of enter phone class
