'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = calc(x)

string = browser.find_element(By.XPATH, '//*[@id="answer"]')
string.send_keys(y)

button2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()



time.sleep(5)
browser.quit()

