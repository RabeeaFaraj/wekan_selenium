from pages.login_page import LoginPage
import unittest
from selenium import webdriver

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:80/sign-in")
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        home = self.login_page.login_as_valid_user("Rabeea.30.03@gmail.com", "30fnhk03")
        self.assertTrue(home.is_logged_in_successfully())

    def tearDown(self):
        self.driver.quit()