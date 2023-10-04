import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button_book = browser.find_element(By.XPATH,'//*[@id="book"]')
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100')
    )
button_book.click()
x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button2 = browser.find_element(By.XPATH,'//*[@id="solve"]')
button2.click()

time.sleep(10)



