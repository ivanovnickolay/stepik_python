from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators

def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(link)
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров (не понятно, так как если выполняется следующее условие то корзина пустая)
    Ожидаем, что есть текст о том что корзина пуста
    :param browser:
    :return:
    """
    mainPage = MainPage(browser, MainPageLocators.LINK)
    mainPage.open()
    mainPage.open_basket()
    basket = BasketPage(browser, "")
    basket.basket_is_empy()
