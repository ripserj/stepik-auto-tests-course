from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from math import log, sin

def calc(x):
    return log(abs(12*sin(x)))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной



button1 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element_by_class_name("btn")
button.click()

input1 = browser.find_element_by_id("input_value")
num1 = input1.text
num = calc(int(num1))
    
input2 = browser.find_element_by_id("answer")
input2.send_keys(str(num)) 
button = browser.find_element_by_id("solve")

browser.execute_script("return arguments[0].scrollIntoView(true);", button)

button.click()

time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()
