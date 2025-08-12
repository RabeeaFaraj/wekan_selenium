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
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.board)
        )        
        self.driver.find_element(*self.board).click() 
        self.driver.find_element(*self.name_board).send_keys(board_name)
        self.driver.find_element(*self.create_button).click()

        
        return BoardPage(self.driver)
        # WebDriverWait(self.driver, 100).until(
        #     EC.presence_of_element_located((By.XPATH, f"//h1[text()='{board_name}']"))
        # )
