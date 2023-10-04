import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(By.XPATH, '//*[@id="book"]')
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By)))
button.click()

time.sleep(5)
