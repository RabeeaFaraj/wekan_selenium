import tempfile
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage # Adjust the import based on your project structure   


class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        if os.getenv("CI"):
            chrome_options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(2)  # מוגדר פעם אחת בלבד

        WEKAN_URL = os.getenv("WEKAN_URL", "http://localhost:80")
        self.driver.get(f"{WEKAN_URL}/sign-in")

        self.login_page = LoginPage(self.driver)


    def test_valid_login(self):
        home = self.login_page.login_as_valid_user("Rabeea.30.03@gmail.com", "30fnhk03")
        self.assertTrue(home.is_logged_in_successfully())
        home.add_board("OOP Programming")
        
    def test_add_board(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
