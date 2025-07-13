from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iphone")
search_box.submit()

wait = WebDriverWait(driver, 10)
first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]//h2/a")))
first_product.click()

wait.until(EC.presence_of_element_located((By.ID, "productTitle")))

product_title = driver.find_element(By.ID, "productTitle").text
print(product_title)

assert "iPhone" in product_title, "Product page does not display product title"
driver.quit()

