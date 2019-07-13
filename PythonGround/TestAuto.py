from selenium import webdriver
# from time import sleep

driver = webdriver.Chrome("E:\AProgTes\SeleniumProjects\seleniumLoad\chromedriver_win32\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("https://www.seleniumhq.org/download/")
# sleep(2)
print(driver.title)
# driver.get_screenshot_as_file("ex: C:\home.png")
driver.maximize_window()
# driver.implcitly_wait(10)
driver.close()
driver.quit()
