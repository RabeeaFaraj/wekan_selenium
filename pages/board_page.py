from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.list = (By.XPATH, "//i[@class='fa fa-plus']")
        self.name_list = (By.XPATH, "//input[@placeholder='Add List']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")

    # def add_list(self, list_name):
    #     # Example method to add a board
    #     # Update selector as needed for your app
    #     self.driver.find_element(*self.board).click() 
    #     self.driver.find_element(*self.name_board).send_keys(board_name)
    #     self.driver.find_element(*self.create_button).click()
    #     return BoardPage(self.driver)
    #     # WebDriverWait(self.driver, 100).until(
    #     #     EC.presence_of_element_located((By.XPATH, f"//h1[text()='{board_name}']"))
    #     # )
