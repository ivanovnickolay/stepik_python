from .base_page import BasePage
from .locators import BasketPageLocator


class BasketPage(BasePage):

    def click_add_to_basket(self):
        self.browser.find_element(*BasketPageLocator.AddToBasket).click()
        self.solve_quiz_and_get_code()

    def basket_is_empy(self):
        """
        Проверка что корзина пустая
        :return:
        """
        text:str = self.browser.find_element_by_css_selector('#content_inner > p').text
        assert text.find("Your basket is empty") != -1, "Your basket is NOT empty"
