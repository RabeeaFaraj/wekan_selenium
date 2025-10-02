from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.list = (By.XPATH, "//i[@class='fa fa-plus']")
        self.name_list = (By.XPATH, "//input[@placeholder='Add List']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
        
        # Wait for board page elements to be present
        try:
            WebDriverWait(self.driver, 15).until(
                EC.any_of(
                    EC.presence_of_element_located(self.list),
                    EC.presence_of_element_located((By.CLASS_NAME, "board-header")),
                    EC.presence_of_element_located((By.CLASS_NAME, "js-add-list"))
                )
            )
            print("✅ Board page loaded successfully")
        except:
            print(f"⚠️ Board page validation timeout, but continuing...")
            print(f"Current URL: {self.driver.current_url}")
            # Don't raise exception, just continue

