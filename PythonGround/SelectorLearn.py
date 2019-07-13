from selenium import webdriver
from selenium.webdriver.common.by import By
# from time import sleep

driver = webdriver.Chrome()
driver.get("https://google.com")

# get the element by selector and pass some text
driver.find_element(By.NAME, "q").send_keys("books")

# get the element and print the selected value
print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
print(driver.find_element(By.NAME, "btnK").get_attribute("value"))
print(driver.find_element(By.NAME, "btnI").get_attribute("value"))

# click on various links and buttons
driver.find_element(By.NAME, "btnK").click()

# sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Google Books").click()
