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
        # Wait for the add board button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.board)
        )
        self.driver.find_element(*self.board).click() 
        
        # Wait for the board name input to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.name_board)
        )
        self.driver.find_element(*self.name_board).send_keys(board_name)
        
        # Wait for create button to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_button)
        )
        self.driver.find_element(*self.create_button).click() 
        
        # Wait for board page to load - look for board-specific elements
        try:
            WebDriverWait(self.driver, 15).until(
                EC.any_of(
                    EC.presence_of_element_located((By.CLASS_NAME, "board-header")),
                    EC.presence_of_element_located((By.CLASS_NAME, "js-add-list")),
                    EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-plus']"))
                )
            )
        except:
            # If specific elements not found, add a small delay and continue
            time.sleep(2)
        
        return BoardPage(self.driver)
       
