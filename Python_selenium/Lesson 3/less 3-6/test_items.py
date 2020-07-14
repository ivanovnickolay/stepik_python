from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


def test_button(browser: webdriver):
    """
        Тестируем наличие кнопки на странице
    :param browser: webdriver
    :return:
    """
    def isElementPresent() -> bool:
        """
        Проверяем наличие элемента, если него нет на странице то "ловим" исключение
        и обрабатываем его
        :rtype: bool
            - True - элемент найден
            - False - элемент не найден
        """
        try:
            browser.find_elements_by_class_name('btn btn-lg btn-primary btn-add-to-basket')
            return True
        except NoSuchElementException:
            return False
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert isElementPresent()==True, "Button not found"
