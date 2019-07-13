from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import signal

driver = webdriver.Chrome()
driver.get('https://skillvalue.com/en/auth/login')
driver.maximize_window()
sleep(3)


