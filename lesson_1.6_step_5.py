'''Импорт библиотек'''
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By #Импортируем библиотеку By
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
import math

link = "http://suninjuly.github.io/find_link_text" # Создаем переменную для ссылки.

try:
    browser = webdriver.Chrome() # Открываем браузер Chrome
    browser.get(link) # Переходим по ссылке указанной в переменной link.

    x = str(math.ceil(math.pow(math.pi, math.e)*10000))
    a1 = browser.find_element(By.LINK_TEXT, x)
    a1.click()


    input1 = browser.find_element(By.TAG_NAME, 'input') # Находим поле для ввода First name
    input1.send_keys("Ivan") #Вводим "Ivan"
    input2 = browser.find_element(By.NAME, 'last_name') # Находим поле для ввода Last name
    input2.send_keys("Petrov") #Вводим "Petrov"
    input3 = browser.find_element(By.CLASS_NAME, 'city') # Находим поле для ввода City
    input3.send_keys("Smolensk") #Вводим "Smolensk"
    input4 = browser.find_element(By.ID, "country") # Находим поле для ввода Country
    input4.send_keys("Russia") #Вводим "Russia"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") # Находим поле для Кнопки
    button.click() # Нажимаем на кнопку

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10) # Пауза 10 секунд
    # закрываем браузер после всех манипуляций
    browser.quit() # Закрываем окно браузера

# не забываем оставить пустую строку в конце файла