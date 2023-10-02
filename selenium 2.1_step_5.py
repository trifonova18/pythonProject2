from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')
    browser.maximize_window()
    
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    print(y)

    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    check.click()

    radio = browser.find_element(By.XPATH, '/html/body/div/form/div[4]/label')
    radio.click()

    submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()