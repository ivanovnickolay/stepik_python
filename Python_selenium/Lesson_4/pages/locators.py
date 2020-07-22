from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BasketPageLocator():
    URL_BASKET_test = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    AddToBasket = (By.CLASS_NAME, "btn-add-to-basket")

class ProductPageLocator():
    url_product = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    # url_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    addProductToBasket = (By.CLASS_NAME, "btn-add-to-basket")
    name_product = (By.CSS_SELECTOR, ".product_main h1")
    message_product = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    price_product = (By.CLASS_NAME,"price_color")
    message_price = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")
    message_suscess = (By.XPATH, '//*[@id="messages"]/div[1]/div')