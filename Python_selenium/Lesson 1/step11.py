from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration2.html"
# link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
browser.get(link)
input1 = browser.find_element_by_css_selector('input.form-control.first:nth-child(2)')
input1.send_keys("Ivan")
input2= browser.find_element_by_css_selector('[placeholder="Input your email"]')
input2.send_keys("mail@mail.ru")
input3 = browser.find_element_by_css_selector('input.form-control.second:nth-child(2)') 
input3.send_keys("Ovsyannikov")

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

#finally:
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()