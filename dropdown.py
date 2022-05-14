from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.maximize_window()

# url = 'https://www.saucedemo.com/'
# driver.get(url)
url = 'http://automationpractice.com/index.php'
driver.get(url)

driver.find_element(By.LINK_TEXT, 'WOMEN').click()
select = Select(driver.find_element(By.TAG_NAME, 'select'))
select.select_by_visible_text('In stock')
# select.select_by_index(1)
# select.select_by_value('name:asc')#value attribute of option tag
