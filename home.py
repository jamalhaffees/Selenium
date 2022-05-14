from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')

driver.maximize_window()

# driver.find_element(By.ID, 'user-name').send_keys('standard_user')
# driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
# driver.find_element(By.CLASS_NAME, 'submit-button').click()



# search_field = driver.find_element(By.NAME, 'q')
# search_field.send_keys('netflix top movies 2022')

print(f'Title of the page is {driver.title}')
print(f'We are working on the {driver.name} browser')
print(driver.current_url)


# html_skeleton = driver.page_source

# print(html_skeleton)

# driver.get('https://www.google.com/')

# driver.back()

# driver.forward()

# ctrl + /

# driver.minimize_window()

# driver.quit()








