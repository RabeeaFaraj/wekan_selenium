from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.home_page import HomePage
           
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "at-field-username_and_email")
        self.password_field = (By.ID, "at-field-password")
        self.login_button = (By.ID, "at-btn")
        
        # Simple validation - don't fail if elements aren't found immediately
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.email_field)
            )
            print("✅ Login page loaded successfully")
        except:
            print("⚠️ Login page elements not immediately visible, continuing...")

    def login_as_valid_user(self, username, password):
        # Simple, direct approach
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        
        # Wait for home page to load
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, "header-main-bar"))
        )
        return HomePage(self.driver)