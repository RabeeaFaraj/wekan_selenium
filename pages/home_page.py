from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.board_page import BoardPage
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.board = (By.CLASS_NAME, "js-add-board")
        self.name_board = (By.CLASS_NAME, "js-new-board-title")
        self.create_button = (By.XPATH, "//input[translate(@value, 'CREATE', 'create')='create']")

    def add_board(self, board_name):
        # Example method to add a board
        # Update selector as needed for your app
        add_board_btn= WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(self.board)
        )        
        add_board_btn.click() 
        self.driver.find_element(*self.name_board).send_keys(board_name)
        self.driver.find_element(*self.create_button).click()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,".swimlane-header.js-open-inlined-form.is-editable.ui-sortable-handle"))
        )
        
        return BoardPage(self.driver)
        # WebDriverWait(self.driver, 100).until(
        #     EC.presence_of_element_located((By.XPATH, f"//h1[text()='{board_name}']"))
        # )
