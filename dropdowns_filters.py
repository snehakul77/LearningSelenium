#Verify that after searching for a specific product for eg : iphone, you want to apply a filter like selecting a brand or price range from a dropdown or sidebar.
#Verify the filtered results

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
filter_brand = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='brandsRefinements']//li[@id='p_123/110955']//i[@class='a-icon a-icon-checkbox']")))
filter_brand.click()


products = driver.find_element(By.XPATH, "//h2[@aria-label='iPhone 16 Pro Max 256 GB: 5G Mobile Phone with Camera Control, 4K 120 fps Dolby Vision and a Huge Leap in Battery Life. Works with AirPods; Desert Titanium']//span[contains(text(),'iPhone 16 Pro Max 256 GB: 5G Mobile Phone with Camera Control, 4K 120 fps Dolby Vision and a Huge Leap in Battery Life. Works with AirPods; Desert Titanium')]")
products.click()

print("test case passed successfully")
print("Able to click on filtered first product")

driver.quit()
