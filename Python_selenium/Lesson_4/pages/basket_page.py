from .base_page import BasePage
from .locators import BasketPageLocator

class BasketPage(BasePage):

    def click_add_to_basket(self):
        self.browser.find_element(*BasketPageLocator.AddToBasket).click()
        self.solve_quiz_and_get_code()

