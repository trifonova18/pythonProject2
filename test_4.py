import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

driver.execute_script('window.scrollTo(0, 500)')
time.sleep(5)
# driver.save_screenshot('screenshot')

action= ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '<a href="https://www.linkedin.com/company/sauce-labs/" target="_blank" rel="noreferrer">LinkedIn</a>')
action.move_to_element(red_t_shirt).perform()

time.sleep(2)
driver.quit()
driver.save_screenshot('screenshot')