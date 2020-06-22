from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name_field = browser.find_element(By.XPATH, "//label[text()='First name*']//following-sibling::input")
    first_name_field.send_keys("First_name")

    last_name_filed = browser.find_element(By.XPATH, "//label[text()='Last name*']//following-sibling::input")
    last_name_filed.send_keys("Last_name")

    email_field = browser.find_element(By.XPATH, "//label[text()='Email*']//following-sibling::input")
    email_field.send_keys("user_email")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
