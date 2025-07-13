#Verify product search on amazon page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

driver.maximize_window()

search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys(" ")
search_box.submit()

time.sleep(3)

assert " " in driver.title or " " in driver.page_source, " Search Results not found for space"

print("test case passed successfully")
driver.quit()

