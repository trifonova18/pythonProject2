from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import pytest


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/file_input.html')
driver.maximize_window()

first_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
first_name.send_keys('Nata')

last_name = driver.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
last_name.send_keys('Trifonova')

email = driver.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
email.send_keys('natalia.o.g@mail.ru')


element = driver.find_element(By.XPATH, '//*[@id="file"]')# добавляем к этому пути имя файла
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'Nata1.txt')
element.send_keys(file_path)

button = driver.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

time.sleep(5)
driver.quit()
