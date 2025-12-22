import traceback

import allure
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.firefox.service import Service as firefoxservice
from utilities import configReader


def before_scenario(context,scenario):
    try:
        if configReader.readConfig("basic info", "browser")== "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--start-maximized')
            context.driver=webdriver.Chrome(service=chromeservice(chromedriver_autoinstaller.install()),options=chrome_options)
        if configReader.readConfig("basic info", "browser")== "firefox":
            firefox_options = webdriver.FirefoxOptions()
            context.driver=webdriver.Firefox(service=firefoxservice(geckodriver_autoinstaller.install()),options=firefox_options)
            context.driver.maximize_window()
    except Exception as e:
        print(f"Exception occured: {e}")
        print(traceback.format_exc())
    context.driver.implicitly_wait(10)

def after_scenario(context,scenario):
    context.driver.quit()

def after_step(context,step):
    print()
    if step.status=='failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)