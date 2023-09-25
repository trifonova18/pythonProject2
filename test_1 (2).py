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
driver.save_screenshot('screenshot')

# text_products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products =='Products'
# print('GOOD')
# url = 'https://www.saucedemo.com/inventory.html'
# get_url = driver.current_url
# print(get_url)
# assert url == get_url
# print('Goood url')

time.sleep(10)
driver.quit()
