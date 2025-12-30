import traceback
import allure
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from selenium.webdriver.firefox.service import Service as firefoxservice
from utilities import configReader

def before_all(context):
    """
        Install drivers ONCE (per worker process) and store the resolved paths.
        NOTE: For CI (Jenkins), it's even safer to pre-install via a pre-build step
        and simply reuse the cache. But this still avoids per-scenario race conditions.
        """
    try:
        # Returns absolute path to the driver exe
        context.chrome_options = webdriver.ChromeOptions()
        context.chrome_options.add_argument('--start-maximized')
        context.chrome_driver_path = chromedriver_autoinstaller.install()
    except Exception as e:
        print(f"[before_all] Chrome driver install failed: {e}")
        print(traceback.format_exc())
        context.chrome_driver_path = None

    try:
        context.gecko_driver_path = geckodriver_autoinstaller.install()
    except Exception as e:
        print(f"[before_all] Geckko driver install failed: {e}")
        print(traceback.format_exc())
        context.gecko_driver_path = None



def before_scenario(context,scenario):
    context.driver = None
    try:
        if configReader.readConfig("basic info", "browser")== "chrome":
            context.driver=webdriver.Chrome(service=chromeservice(context.chrome_driver_path),options=context.chrome_options)
        if configReader.readConfig("basic info", "browser")== "firefox":
            firefox_options = webdriver.FirefoxOptions()
            context.driver=webdriver.Firefox(service=firefoxservice(context.gecko_driver_path),options=firefox_options)
            context.driver.maximize_window()
    except Exception as e:
        print(f"Exception occured: {e}")
        print(traceback.format_exc())
    context.driver.implicitly_wait(10)

def after_scenario(context,scenario):
    if getattr(context, "driver", None):
        try:
            context.driver.quit()
        except Exception:
            pass
        finally:
            context.driver = None


def after_all(context):
    # Defensively quit if any driver is still around
    if getattr(context, "driver", None):
        try:
            context.driver.quit()
        except Exception:
            pass
        finally:
            context.driver = None


def after_step(context,step):
    print()
    if step.status.name =='failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)