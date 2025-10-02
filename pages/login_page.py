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
        # try:
        #     # Wait for either the auth dialog OR the email field to appear
        #     WebDriverWait(self.driver, 60).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "auth-dialog")),
        #     )
            
        # except:
        #     # Capture page source for debugging in CI
        #     raise Exception("Login page not loaded. Check WEKAN_URL or network access.")
        # Wait for login form elements to be present instead of auth-dialog
        try:
            WebDriverWait(self.driver, 10).until(
                EC.any_of(
                    EC.presence_of_element_located(self.email_field),
                    EC.presence_of_element_located(self.password_field),
                    EC.presence_of_element_located(self.login_button)
                )
            )
            print("✅ Login page loaded successfully")
        except:
            print(f"❌ Login page validation failed")
            print(f"🔍 Current URL: {self.driver.current_url}")
            print(f"📄 Page title: {self.driver.title}")
            raise Exception("Login page not loaded successfully")
        

    def login_as_valid_user(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
         # Wait for the home page to load (adjust selector as needed)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.ID, "header-main-bar"))
        )
        return HomePage(self.driver)
    

