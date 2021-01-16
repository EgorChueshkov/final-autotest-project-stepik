from selenium import webdriver
import time


link = "http://selenium1py.pythonanywhere.com/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".basket-mini a.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()