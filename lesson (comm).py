'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By

'''Окрываем окно браузера и переходим по ссылке'''
driver = webdriver.Chrome() # Открываем браузер Chrome
driver.get('https://www.saucedemo.com/') # Переходим по ссылке
driver.maximize_window() # Расширяем окно браузера на весь экран

'''Находим и заполняем поля логин и пароль. Нажимаем на кнопку Отправить.'''
user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') # Находим поле для ввода логина
user_name.send_keys('standard_user') # Вводим логин 'standard_user'

password = driver.find_element(By.CSS_SELECTOR, '#password')  # Находим поле для ввода пароля
password.send_keys('secret_sauce') # Вводим пароль 'secret_sauce'

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]') # Находим элемент с кнопкой
button_login.click() # Нажимаем на кнопку

'''Ждём 10 секунд. Закрываем окно браузера'''
time.sleep(10) # Пауза 10 секунд
driver.close() # Закрываем окно браузера