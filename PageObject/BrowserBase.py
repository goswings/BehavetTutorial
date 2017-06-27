from selenium import webdriver
from Common.SeleniumCommonBase import SeleniumCommon

class Browser(SeleniumCommon):
    def close(context):
        context.driver.quit()

