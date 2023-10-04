import pytest

from lesson import driver

'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By

@pytest.fixture
def set_up():
    driver = webdriver.Chrome()  # Открываем браузер Chrome
    driver.get('https://www.saucedemo.com/')  # Переходим по ссылке
    driver.maximize_window()  # Расширяем окно браузера на весь экран
    yield
    driver.close()  # Закрываем окно браузера
def test_test_1_mail_1_09_10(set_up):
    user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # Находим поле для ввода логина
    user_name.send_keys('standard_user')  # Вводим логин 'standard_user'

    password = driver.find_element(By.CSS_SELECTOR, '#password')  # Находим поле для ввода пароля
    password.send_keys('secret_sauce')  # Вводим пароль 'secret_sauce'

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')  # Находим элемент с кнопкой
    button_login.click()  # Нажимаем на кнопку

def test_login_2_mail_2(set_up):
    pass
def test_login_3_mail_2(set_up):
    pass
def test_login_4_mail_2(set_up):
    pass

time.sleep(5)
