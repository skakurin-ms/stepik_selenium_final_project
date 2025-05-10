# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='en',
#                      help="Enter any language (e.g. ru, es, en and etc...")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     print("\nstart browser for test..")
#     language = request.config.getoption("language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': language})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

#solution 2
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language (e.g. enter: en, es, ru...")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

