import unittest
from Infrastructure.BasicTest import BasicTestClass
from FrancoManca.PageObjects import *


class FmTestsClass(BasicTestClass, unittest.TestCase):
    def test_100_OpenFm(self):
        FmHomePage.openLoginPage()


if __name__ == "__main__":
    unittest.main()
