import tempfile
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage # Adjust the import based on your project structure   
from pages.login_page import HomePage
from pages.board_page import BoardPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1280,800")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")    
        chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

        if os.getenv("CI","False") == "true":
            chrome_options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(20)  # מוגדר פעם אחת בלבד

        WEKAN_URL = os.getenv("WEKAN_URL", "http://localhost:80")
        self.driver.get(f"{WEKAN_URL}/sign-in")
        self.login_page = LoginPage(self.driver)


    def test_valid_login(self):
        homePage = (
            self.login_page
            .login_as_valid_user("Rabeea.30.03@gmail.com", "123456789")
        )
        self.assertIsInstance(homePage, HomePage, "home is not an instance of BoardPage")
        print("\nLogin successful, home page loaded\n")


    # def test_add_board(self):
    #     add_board = (
    #         self.login_page
    #         .login_as_valid_user("Rabeea.30.03@gmail.com", "123456789")
    #         .add_board("OOP Programming")
    #     )
    #     self.assertIsInstance(add_board, BoardPage, "add_board is not an instance of BoardPage")
    #     print("\nBoard added successfully, board page loaded\n")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
