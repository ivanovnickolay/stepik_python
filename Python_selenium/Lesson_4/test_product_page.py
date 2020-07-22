import time

import pytest
from selenium.webdriver.common.by import By

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
