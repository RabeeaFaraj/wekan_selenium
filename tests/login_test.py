from pages.login_page import LoginPage
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless=new")  # מריץ בלי GUI
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-profile")  # פרופיל זמני

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        # at the top of your file
        WEKAN_URL = os.getenv("WEKAN_URL", "http://localhost:80")

        # in setUp()
        self.driver.get(f"{WEKAN_URL}/sign-in")
        #self.driver.get("http://localhost:80/sign-in")
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        home = self.login_page.login_as_valid_user("Rabeea.30.03@gmail.com", "30fnhk03")
        self.assertTrue(home.is_logged_in_successfully())

    def tearDown(self):
        self.driver.quit()
