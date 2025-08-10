from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
           
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "at-field-username_and_email")
        self.password_field = (By.ID, "at-field-password")
        self.login_button = (By.ID, "at-btn")

        self.driver.implicitly_wait(2)
        
        # Correct way to check for class presence
        try:
            self.driver.find_element(By.CLASS_NAME, "auth-dialog")
        except:
            raise Exception("Login page not loaded successfully")
        

    def login_as_valid_user(self, username, password):
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
         # Wait for the home page to load (adjust selector as needed)
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, "header-main-bar"))
        )
        return HomePage(self.driver)
    

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_logged_in_successfully(self):
        # Example: check for an element only visible after login
        # Update selector as needed for your app
        try:
            self.driver.find_element(By.ID, "header-main-bar")
            return True
        except:
            return False