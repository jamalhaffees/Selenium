from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://automationpractice.com/index.php')

add_buttons = driver.find_elements(By.CLASS_NAME, "product-container")

print(f'There are {len(add_buttons)} products displayed')

add_buttons[0].click()

driver.find_element(By.NAME, "Submit").click()

print(f'There is 1 item in your cart'in driver.page_source)