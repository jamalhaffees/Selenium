from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')

driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.CLASS_NAME, 'submit-button').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.TAG_NAME, 'button').click()

driver.find_element(By.CLASS_NAME, 'inventory_item_name')
print('Sauce Labs Bike Light')





#driver.find_element(By.CLASS_NAME, 'inventory_item_name').send_keys('Sauce Labs Bolt T-Shirt')
# print(f'Title of the page is {driver.title}')
# print(f'Browser name {driver.name}')
# print(driver.current_url)



# driver.get('https://www.google.com/')

# driver.maximize_window()

# driver.get('https://www.yahoo.com/')

# driver.back()

# driver.forward()

# driver.minimize_window()

# driver.close()
