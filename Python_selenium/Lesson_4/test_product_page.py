from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocator

"""
Тестирование добавления продукта в корзину
"""

def test_add_product(browser):
    page = ProductPage(browser, ProductPageLocator.url_product)
    page.open()
    page.addProductToBasket()