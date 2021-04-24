import unittest
from selenium import webdriver
from Pages.Login import LoginPage
from Pages.HomePage import HomePage
import time


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
        cls.driver.maximize_window()

    def test_login_functionality(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        time.sleep(5)
        homepage.click_logout_link()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
