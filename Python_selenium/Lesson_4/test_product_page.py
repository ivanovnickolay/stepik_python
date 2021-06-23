import time

import pytest
from .pages.basket_page import BasketPage

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocator

"""
Тестирование добавления продукта в корзину
"""

def test_add_product(browser):
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.addProductToBasket()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.addProductToBasket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
        - Открываем страницу товара
        - Добавляем товар в корзину
        - Проверяем, что нет сообщения об успехе с помощью is_not_element_present

        :return:
    """

    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.click_add_button()
    assert page.is_not_element_present(*ProductPageLocator.message_suscess),"Success message is presented, but should " \
                                                                            "not be "


def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    :param browser:
    :return:
    """
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    assert page.is_not_element_present(
        *ProductPageLocator.message_suscess), "Success message is presented, but should not be"

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    :param browser:
    :return:
    """
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.click_add_button()
    time.sleep(1)
    assert page.is_disappeared(
        *ProductPageLocator.message_suscess), "Success message is presented, but should not be"


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Тест сценария :  гость может перейти на страницу логина со страницы Х
    :param browser:
    :return:
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Тест сценария :  гость может перейти на страницу логина со страницы продукта
    :param browser:
    :return:
    """
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров (не понятно, так как если выполняется следующее условие то корзина пустая)
    Ожидаем, что есть текст о том что корзина пуста
    :param browser:
    :return:
    """
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.open_basket()
    basket = BasketPage(browser, "")
    basket.basket_is_empy()