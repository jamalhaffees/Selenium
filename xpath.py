from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.maximize_window()

url = 'http://automationpractice.com/index.php'
driver.get(url)

driver.find_element(By.XPATH, "//a[text()='Contact us']").click()
select= Select(driver.find_element(By.TAG_NAME, 'select'))

select.select_by_visible_text('Customer service')
select.select_by_index(1)
driver.find_element(By.CSS_SELECTOR,'#email').send_keys("team@skillrill.com")
driver.find_element(By.CSS_SELECTOR,'#id_order').send_keys(1)
driver.find_element(By.XPATH,"//*[@id='fileUpload']").send_keys(r'C:\SkillRill\Selenium\test.txt')


driver.find_element(By.CSS_SELECTOR, "#message").send_keys('test')
driver.find_element(By.XPATH, "//span[text()='Send']").click()



