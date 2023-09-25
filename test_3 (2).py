import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys(login_standard_user)
print('Input Login')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
print('Input Password')
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
filter.click()
print('Click Filter')
filter.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)
time.sleep(10)
driver.close()