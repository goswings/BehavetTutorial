from selenium.webdriver.common.by import By
from PageObject.BrowserBase import Browser

class GooglePage(Browser):
    def __init__(self,driver):
        self.driver = driver
        self.SearchText = (By.ID,'lst-ib')
        self.SearchButton = (By.CLASS_NAME ,'lsb')

    def SearchValue(self, value):
        self.send_key_with_Element(self.SearchText,value)
        self.locateElement(self.SearchButton).click()

