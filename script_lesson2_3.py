from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)  # Исправлено: добавлена закрывающая скобка

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

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
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

