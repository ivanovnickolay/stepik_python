import pytest
from selenium import webdriver
import time
import math


text_correct = ''

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
])
def test_(browser, link):
    # browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe')
    browser.get(link)
    browser.implicitly_wait(10)
    textarea = browser.find_element_by_class_name('ember-text-area')
    textarea.send_keys((str(math.log(int(time.time())))))
    browser.find_element_by_class_name('submit-submission').click()
    browser.implicitly_wait(10)
    txt = browser.find_element_by_class_name('attempt-message_correct').text
    is_correct = browser.find_element_by_class_name("smart-hints__hint").text
    assert is_correct == "Correct!", f"expected {is_correct}, got Correct!"
    # browser.quit()


