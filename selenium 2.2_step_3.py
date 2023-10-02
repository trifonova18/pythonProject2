from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
browser.maximize_window()

num1 = browser.find_element(By.XPATH, '//*[@id="num1"]')
num1 = num1.text
print(num1)


num2 = browser.find_element(By.XPATH, '//*[@id="num2"]')
num2 = num2.text
print(num2)


y = int(num1)+int(num2)
y = str(y)

string = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
string.select_by_visible_text(y)

button = browser.find_element(By.XPATH, '/html/body/div/form/button')
button.click()

time.sleep(5)
