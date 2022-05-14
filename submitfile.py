from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://automationpractice.com/index.php'
driver.get(url)

driver.find_element(By.XPATH,"//a[text()='Contact Us']").click()
# driver.find_element(By.CSS_SELECTOR, "#fileupload").send_keys(r'C:\AUTOMATION\Ebang\1.txt')

# choose_file = driver.find_element(By.CSS_SELECTOR, "#fileupload")
# choose_file.send_keys(r'C:\AUTOMATION\Ebang\1.txt')