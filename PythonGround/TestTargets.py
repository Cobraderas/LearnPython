from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import signal


driver = webdriver.Chrome()
driver.get('https://skillvalue.com/en/auth/login')
driver.maximize_window()
sleep(3)

# log-in
#driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys("cata.catal0101+13@gmail.com")
#driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("zaqwsx123!@#")
#driver.find_element(By.XPATH, "//button[@class = 'btn btn-submit']").click()
#sleep(3)

# mouse hover an item :
#firstLevelMenu = driver.find_element(By.XPATH, "//li[@class='menu-item dropdown menu-button profile']")
#action.move_to_element(firstLevelMenu).perform()
#sleep(3)
#thirdLevelMenu = driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]")
#action.move_to_element(thirdLevelMenu).perform()
#thirdLevelMenu.click()

# mouse hover action with select flag and switch language
driver.get('https://skillvalue.com/en')
action = ActionChains(driver)
sleep(2)
enFlagMenu = driver.find_element(By.XPATH, "//a[@class='button-flag flag-en is-active']")
action.move_to_element(enFlagMenu).perform()
sleep(2)
frFlagMenu = driver.find_element_by_xpath("//a[@class='button-flag flag-fr']")
action.move_to_element(frFlagMenu).perform()
frFlagMenu.click()



