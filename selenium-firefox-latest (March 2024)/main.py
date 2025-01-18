# Mostly Deprecated

# This is a basic example of how to utilize selenium for firefox (GeckoDriver) in Python.
# Included is initializing the driver and setting config options.
# Then we navigate to the target website url.
# Provided is a function for finding elements by XPath.
# Finally an example shows how to use an elements XPath to locate it in the document and perform inputs on the element.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# The getXPath function takes two parameters, the driver and the xpath to search for.
# This function returns the element if found, otherwise, None will be returned
def getXPath(driver, xpath):
    element = None
    # Error handling
    try:
        # Utilizes the Selenium built in wait function to ensure element is given time to load
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except Exception as e:
        print(e)
    return element

def example(driver):
    # Get target website
    driver.get("ENTER TARGET URL HERE")
    
    # Get element by xpath
    element = getXPath(driver, 'ENTER XPATH')
    # Common inputs, clicking element and sending keystrokes
    element.click()
    element.send_keys("asjfgyasdufgas")

def main():
    # Initialize driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.set_window_size(800, 800)
    
    example(driver)

if __name__ == "__main__":
    main()