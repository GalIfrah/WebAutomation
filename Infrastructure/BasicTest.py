from Infrastructure.WebDriverWrapper import Wrapper


class BasicTestClass:

    driver = Wrapper()
    platform = ''

    def setUp(self):
        if self.platform == "desktop":
            print('init the remote webdriver')
            print(BasicTestClass.platform)
            BasicTestClass.driver.initDesktop('http://localhost:4444/wd/hub')

        if self.platform == "mobile":
            print('init the mobile remote webdriver')
            self.driver.initMobile('http://localhost:4444/wd/hub', 'iPhone X')

    def tearDown(self):
        print('test ended')
        print('**************************************')
        # self.driver.closeCurrent()