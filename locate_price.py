#verify price of 1st product after iphone search

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import wait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iphone")
search_box.submit()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@data-component-type = 's-search-results']")))

price_whole = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result'])[1]//span[@class='a-price-whole']").text
price_fraction = driver.find_element(By.XPATH,"(//div[@data-component-type='s-search-result'])[1]//span[@class='a-price-fraction']").text

full_price = f"{price_whole}.{price_fraction}"
print("first product price: ", full_price)

driver.quit()




