#Verify Launching Amazon and Verifying the Homepage Loads Successfully

import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in")
driver.implicitly_wait(10)

assert "Amazon" in driver.title, "Amazon is in the title"

driver.quit()


