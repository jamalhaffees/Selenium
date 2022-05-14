from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://www.seleniumframework.com/Practiceform/'
driver.get(url)

alert_button = driver.find_element(By.CSS_SELECTOR, '#alert')
alert_button.click()

alert = driver.switch_to.alert
sleep(5)
alert.accept()