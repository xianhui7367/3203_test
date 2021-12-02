import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    """
    setup of browser, to be passed in for each ui test
    """
    # setup
    options = Options()
    options.headless = True  # False for non-headless
    s = Firefox_Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=s, options=options)

    # return when completed
    yield browser


def test_http(browser):
    # setup
    wait = WebDriverWait(browser, 10)
    browser.get("http://apptest:5000")
    #     wait.until(EC.title_is("127.0.0.1:5000"))

    # check for https connection
    assert "http" in browser.current_url
    browser.close()

#