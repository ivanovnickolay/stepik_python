import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Languare...")


@pytest.fixture(scope="function")
def browser(request) -> webdriver:
    """
    При запуске обращать особое внимание на строку
    webdriver.Chrome('../ChromeDriver/chromedriver.exe',chrome_options=options)
        -   '../ChromeDriver/chromedriver.exe' путь к драйверу
        -   chrome_options=options параметры опций отличаются от указаных в лекциях
    :param request:
    :return:
    """
    browser_name = request.config.getoption("browser_name")
    languare_name = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': languare_name})
        browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe',chrome_options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': languare_name})
        browser = webdriver.Chrome('../ChromeDriver/chromedriver.exe', chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# @pytest.fixture(scope="function")
# def language_name(request):
#     languare_name = request.config.getoption("language")
#     return languare_name

