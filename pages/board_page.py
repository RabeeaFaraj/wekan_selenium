from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.list = (By.XPATH, "//i[@class='fa fa-plus']")
        self.name_list = (By.XPATH, "//input[@placeholder='Add List']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")

