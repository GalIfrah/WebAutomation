from TestsClassesInit import *




class Tests(BasicTestClass, unittest.TestCase):

    def test_100_chooseFirstCategory(self):
        Connect.login()

        HomePage.startOrder(1)

        Menu.chooseSecondCategory()

        self.assertTrue(Menu.checkIfCategoryChosen() is True, ErrorsHandler.ELEMENT_NOT_VISIBLE)