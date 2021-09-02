from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
from math import log, sin

import os 






def calc(x):
    return log(abs(12*sin(x)))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
            
    button = browser.find_element_by_class_name("btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    
 #   alert = browser.switch_to.alert
 #   alert.accept()
    
    input1 = browser.find_element_by_id("input_value")
    num1 = input1.text
    num = calc(int(num1))
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(num))     
    
    
#    input1 = browser.find_element_by_name("firstname")
##    input1.send_keys("Ivan")
#    input2 = browser.find_element_by_name("lastname")
#    input2.send_keys("Ivanov")
#    input3 = browser.find_element_by_name("email")
#    input3.send_keys("Ivanov@yandex.ru")    

#    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#    file_path = os.path.join(current_dir, 'file1.txt')           # добавляем к этому пути имя файла      
    
#    link = browser.find_element_by_id("file")
#    link.send_keys(file_path)


    button = browser.find_element_by_class_name("btn")
    button.click()
    
#    pict_num = pict.get_attribute("valuex")
 #   num = int(num1) + int(num2)
 #   print(num)
 #   select = Select(browser.find_element_by_tag_name("select"))
 #   select.select_by_value(str(num)) # ищем элемент с текстом "Python"
    
   # input1 = browser.find_element_by_id("answer")
  #  input1.send_keys(str(num))    
    
  #  link = browser.find_element_by_id("robotCheckbox")
  #  link.click()
  ##  link = browser.find_element_by_id("robotsRule")
  #  browser.execute_script("return arguments[0].scrollIntoView(true);", link)
  #  link.click()
  #  button = browser.find_element_by_class_name("btn")
  #  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
       
    
  #  button = browser.find_element_by_xpath("//button[text()='Submit']")
 #   button.click()
 #   button.click()  
    #treasure
    
  #  text = str(math.ceil(math.pow(math.pi, math.e)*10000))
 #   print(text)
    
#    link = browser.find_element_by_link_text(text)
#    link.click()

   # input1 = browser.find_element_by_tag_name(".form-control[name='first_name']")
  #  input1.send_keys("Ivan")
  #  input2 = browser.find_element_by_name("last_name")
  #  input2.send_keys("Petrov")
  #  input3 = browser.find_element_by_class_name("city")
  #  input3.send_keys("Smolensk")
  #  input4 = browser.find_element_by_id("country")
  #  input4.send_keys("Russia")


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла