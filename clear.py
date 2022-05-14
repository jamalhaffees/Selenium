
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://www.saucedemo.com/'
driver.get(url)

driver.maximize_window()

username = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys('test')
# driver.find_element(By.CSS_SELECTOR, "#user-name").clear()

element = driver.find_element(By.XPATH, "//div[@class='login_password']/h4")
