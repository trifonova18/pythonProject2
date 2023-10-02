import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog')
driver.maximize_window()
time.sleep(5)
login = driver.find_element(By.XPATH, '//*[@id="ember245"]')
login.click()

user_name = driver.find_element(By.XPATH, '//*[@id="id_login_email"]')
user_name.send_keys('natalia.o.g@mail.ru')

password = driver.find_element(By.XPATH, '//*[@id="id_login_password"]')
password.send_keys('156')

button = driver.find_element(By.XPATH, '//*[@id="login_form"]/button')
button.click()

time.sleep(5)
driver.close()


