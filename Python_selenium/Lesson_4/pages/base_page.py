from selenium import webdriver


class BasePage():
    def __init__(self, browser, url):
        self.browser: webdriver = browser
        self.url: str = url

    def open(self):
        self.browser.get(self.url)
