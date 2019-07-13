#!/usr/bin/env python
#!/usr/bin/python

import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import signal

browser = webdriver.Firefox()
browser.get('http://www.ubuntu.com/')


browser = webdriver.Chrome()
browser.get('http://www.ubuntu.com/')
print(sys.version)

driver.find_element(By.NAME, "btnK").click()
driver.find_element(By.NAME, "q").send_keys("books")
print(driver.find_element(By.TAG_NAME, "img").get_attribute("src"))
driver.set_page_load_timeout(20)
print(driver.title)
sleep(2)
driver.get_screenshot_as_file("ex: C:\home.png")
driver.maximize_window()
driver.implcitly_wait(10)
driver.close()
driver.quit()


browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

def hover(browser, xpath):
    element_to_hover_over = browser.find_element_by_xpath(xpath)
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()



# mouse hover an item :
action = ActionChains(driver)
firstLevelMenu = driver.find_element(By.XPATH, "//a[@class='button-flag flag-en is-active']")
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = driver.find_element_by_xpath("//a[@class='button-flag flag-fr']")
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()



# use of implicit wait with try except
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('url')
timeout = 5
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print "Timed out waiting for page to load"


#scroll until the end example
def scrollDown(driver, value):
    driver.execute_script("window.scrollBy(0,"+str(value)+")")

# Scroll down the page
def scrollDownAllTheWay(driver):
    old_page = driver.page_source
    while True:
        logging.debug("Scrolling loop")
        for i in range(2):
            scrollDown(driver, 500)
            time.sleep(2)
        new_page = driver.page_source
        if new_page != old_page:
            old_page = new_page
        else:
            break
    return True

http://allselenium.info/wait-for-elements-python-selenium-webdriver/


    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait

    driver = webdriver.Chrome("E:\\Python\\selenium\\webdriver\\chromedriver.exe")
    driver.get("https://www.tatacliq.com/global-desi-navy-embroidered-kurta/p-mp000000000876745")
    driver.set_page_load_timeout(45)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get_screenshot_as_file("E:\\Python\\Tatacliq.png")
    print("Executed Succesfull")
    driver.find_element_by_xpath("//div[@class='pdp-promo-title pdp-title']").click()
    `enter
    code
    here
    `
    SpecialPrice = driver.find_element_by_xpath("//div[@class='pdp-promo-title pdp-title']").text
    print(SpecialPrice)