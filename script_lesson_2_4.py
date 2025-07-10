from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)  

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    button.click()


    # Явное ожидание для элемента x
    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
	
	
    x = x_element.text  # Получаем текст элемента
    y = calc(x)

    # Явное ожидание для элемента y
    y_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "answer"))
    )
    y_element.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    button.click()



finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

