from Infrastructure.WebDriverWrapper import Wrapper


class BasicTestClass:
    driver = Wrapper()
    platform = None

    def setUp(self):
        if self.platform == "desktop":
            print('init the remote webdriver')
            print(BasicTestClass.platform)
            BasicTestClass.driver.initDesktop('http://localhost:4444/wd/hub')

        if self.platform == "mobile":
            print('init the remote webdriver')
            self.driver.initMobile('http://localhost:4444/wd/hub', 'iPhone 5/SE')

    def tearDown(self):
        print('test ended')
        print('**************************************')
