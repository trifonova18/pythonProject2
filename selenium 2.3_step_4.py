'''Импорт библиотек'''
import math
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
browser.maximize_window()

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button1.click()

time.sleep(5)
browser.quit()

