'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://www.gov.spb.ru/')
driver.maximize_window()

search_bar = driver.find_element(By.XPATH, '//*[@id="search_text"]')
search_bar.send_keys('бюджет Санкт-Петербурга')

search_bar = driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
search_bar.click()

time.sleep(5)
driver.close()




