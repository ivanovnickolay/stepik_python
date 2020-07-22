from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser: RemoteWebDriver, url,  timeout=10):
        self.browser = browser
        self.url: str = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        """
        is_not_element_present: упадет, как только увидит искомый элемент.
        Не появился: успех, тест зеленый.
        https://stepik.org/lesson/201964/step/5?unit=176022
        абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени

        Пример использования

        def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

        :param self:
        :param how:
        :param what:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        is_disappeared: будет ждать до тех пор, пока элемент не исчезнет.
        https://stepik.org/lesson/201964/step/5?unit=176022
        Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться
        явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем

        :param self:
        :param how:
        :param what:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True