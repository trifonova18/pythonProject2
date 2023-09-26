import time
from selenium import webdriver
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
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print('Click Login Button')

menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
menu.click()
print('click menu button')

time.sleep(10)
link_about = driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
link_about.click()
print("click Link Button")


time.sleep(10)
driver.close()
