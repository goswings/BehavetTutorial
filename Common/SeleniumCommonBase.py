from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import requests

class SeleniumCommon(object):
    def __init__(self):
        #self.driver = driver
        self.driver.implicitly_wait(15)

    def open(self,URL):
        self.driver.get(URL)

    def driverURLChange(self,URL):
        print("change URL" + URL)
        self.driver.get(URL)

    def currentUrl(self):
        print("URL   " +  self.driver.current_url)
        return self.driver.current_url

    def switchNewWindow(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.title

    def send_key_with_Element(self,loc,value):
        self.locateElement(loc).click()
        self.locateElement(loc).clear()
        self.locateElement(loc).send_keys(value)

    def locateElement(self,loc):
        try:
            print(loc)
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return element
        except:
            print("cannot find {0} element".format(loc))
        return None

    def locateMutipleElements(self,loc):
        try:
            print(loc)
            elements = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(loc))
            return elements
        except:
            print ("cannot find {0} element".format(loc))

    def locateangularElement(self,loc):
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, loc)))
            return element
        except:
            print ("cannot find {0} element".format(loc))
        return None

    def waitForElementInvisible(self,loc):
        #load-spinner
        try:
            element = WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loc))
            return True
        except:
            print ("cannot invisibility_of_element {0} element".format(loc))
        return False

    def waitForElementVisible(self,loc):
        #load-spinner
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of(loc))
            return True
        except:
            print ("cannot visibility_of_element {0} element".format(loc))
        return False

    def click_with_Element(self, loc):
        self.locateElement(loc).click()

    def clickElementsBySendKey(self, loc, value):
        self.locateElement(loc).send_keys(value)

    def checkSourceHaveErrorOrNot(self):
        request = requests.get(self.currentUrl())
        return request.status_code == 404 or request.status_code == 500

    def selectElementByVisibleText(self, loc, value):
        selectElement = Select(self.locateElement(loc))
        selectElement.select_by_visible_text(value)

    def selectElementByValue(self, loc, value):
        selectElement = Select(self.locateElement(loc))
        selectElement.select_by_value(value)

    def moveToElement(self, element):
        hoverElement = ActionChains(self.driver).move_to_element(element)
        print("move")
        hoverElement.perform()

    def closeWindowAndSwitchBack(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def saveScreenShot(self, fileName):
        self.driver.save_screenshot(fileName)

    def backPage(self):
        self.driver.back()

    def quit(self):
        self.driver.quit()

