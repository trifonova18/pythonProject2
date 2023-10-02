from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
browser.maximize_window()

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = x.text
y = calc(x)
print(y)



browser.execute_script("window.scrollBy(0, 100);")
import1 = browser.find_element(By.XPATH, '/html/body/div/form/button')
import1.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
answer.send_keys(y)

check = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
check.click()

radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
radio.click()

submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
submit.click()


time.sleep(10)
browser.quit()