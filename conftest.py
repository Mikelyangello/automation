import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from globals import MyCreds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    try:
        browser.quit()
    except Exception:
        pass


@pytest.fixture(scope="session")
def mc():
    return MyCreds()


@pytest.fixture(scope="session")
def by():
    return By


@pytest.fixture(scope="session")
def wd():
    return WebDriverWait


@pytest.fixture(scope="session")
def ec():
    return expected_conditions
