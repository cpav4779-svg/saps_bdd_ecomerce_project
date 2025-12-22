import logging

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.utilities.logUtil import Logger
from features.utilities import configReader
log=Logger(__name__,logging.INFO)

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def openUrl(self,url):
        self.driver.get(configReader.readConfig("basic info",url))

    def clickElement(self,locator):
        if str(locator).lower().endswith("_xpath"):
            self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator)).click()
        elif str(locator).lower().endswith("_css"):
            self.driver.find_element(By.CSS_SELECTOR,configReader.readConfig("locators",locator)).click()
        elif str(locator).lower().endswith("_id"):
            self.driver.find_element(By.ID,configReader.readConfig("locators",locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self,locator,value):
        if str(locator).lower().endswith("_xpath"):
            self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator)).send_keys(value)
        elif str(locator).lower().endswith("_css"):
            self.driver.find_element(By.CSS_SELECTOR,configReader.readConfig("locators",locator)).click()
        elif str(locator).lower().endswith("_id"):
            self.driver.find_element(By.ID,configReader.readConfig("locators",locator)).send_keys(value)

    def select(self,locator,value):
        global dropdown
        if str(locator).lower().endswith("_xpath"):
            dropdown = self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_css"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_id"):
            dropdown = self.driver.find_element(By.ID,configReader.readConfig("locators",locator))
        dropdown = Select(dropdown)
        dropdown.select_by_visible_text(value)
        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    def moveTo(self,locator):
        if str(locator).lower().endswith("_xpath"):
            element=self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_css"):
            element=self.driver.find_element(By.CSS_SELECTOR,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_id"):
            element=self.driver.find_element(By.ID,configReader.readConfig("locators",locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(locator))

    def implicit_wait(self,time=10):
        self.driver.implicitly_wait(time)

    def explicit_wait_object(self,time=10):
        wait=WebDriverWait(self.driver,time)

    def find_the_elements(self,locator):
        global elements
        if str(locator).lower().endswith("_xpath"):
            elements=self.driver.find_elements(By.XPATH,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_css"):
            elements=self.driver.find_elements(By.CSS_SELECTOR,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_id"):
            elements=self.driver.find_elements(By.ID,configReader.readConfig("locators",locator))
        return elements

    def find_the_element(self,locator):
        global element
        if str(locator).lower().endswith("_xpath"):
            element=self.driver.find_element(By.XPATH,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_css"):
            element=self.driver.find_element(By.CSS_SELECTOR,configReader.readConfig("locators",locator))
        elif str(locator).lower().endswith("_id"):
            element=self.driver.find_element(By.ID,configReader.readConfig("locators",locator))
        return element



















