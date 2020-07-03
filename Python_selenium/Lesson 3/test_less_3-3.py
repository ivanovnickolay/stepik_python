import unittest
from selenium import webdriver
import time


class test(unittest.TestCase):
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block div.second_class input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block div.third_class input.third")
        input3.send_keys("1@1.ua")

        # Отправляем заполненную форму
        button = browser.find_element_by_tag_name("button[type='submit']")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, 'text not found')
        browser.quit()

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        # пусть в chromedriver
        browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block div.second_class input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block div.third_class input.third")
        input3.send_keys("1@1.ua")

        # Отправляем заполненную форму
        button = browser.find_element_by_tag_name("button[type='submit']")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'text not found')
        browser.quit()
