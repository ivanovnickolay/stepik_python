import time

from .base_page import BasePage
from .locators import ProductPageLocator

"""
Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209).
Нажимаем на кнопку "Добавить в корзину".
Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
"""


class ProductPage(BasePage):

    def addProductToBasket(self):
        """
        тестирование добавление продукта в корзину
        """
        self.is_add_basket_button()
        self.click_add_button()
        self.solve_quiz_and_get_code()
        self.message_name_product_add()
        self.message_price_product_add()
        # time.sleep(10)

    def is_add_basket_button(self):
        """
        Проверим есть ли кнопка "Добавить в корзину
        :return:
        """
        assert self.is_element_present(*ProductPageLocator.addProductToBasket), "Button add to basket not found"

    def click_add_button(self):
        self.browser.find_element(*ProductPageLocator.addProductToBasket).click()

    def message_name_product_add(self):
        """
        Проверим что товар действительно добавлен
        :return:
        """

        name_product = self.browser.find_element(*ProductPageLocator.name_product).text
        message_product: str = self.browser.find_element(*ProductPageLocator.message_product).text
        assert message_product == name_product, "Product not add to basket"

    def message_price_product_add(self):
        """
        Проверим что товар действительно добавлен
        :return:
        """
        price_product = self.browser.find_element(*ProductPageLocator.price_product).text
        message_price: str = self.browser.find_element(*ProductPageLocator.message_price).text
        assert message_price.find(price_product) != -1, "Product price not add to basket"
