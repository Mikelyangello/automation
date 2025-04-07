import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Enter your prefer language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.chrome.options.Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxProfile()
        options.set_preference("intl.accept_languages", user_language)
        options.binary_location = r'C:\Program Files\Mozilla Firefox'
        browser = webdriver.Firefox()
    yield browser
    delay = 10
    print(f"\nquit browser.. with delay --- {delay}sec.")
    time.sleep(delay)
    try:
        browser.quit()
    except Exception:
        pass


@pytest.fixture(scope="session")
def by():
    return By
