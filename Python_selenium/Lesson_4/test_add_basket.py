from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocator
from selenium.common.exceptions import NoAlertPresentException # в начале файла

def test_add_to_basket(browser):
    page = BasketPage(browser, BasketPageLocator.URL_BASKET_test)
    page.open()
    page.click_add_to_basket()