import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=en,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    
    browser = webdriver.Chrome()
    browser.get( "http://selenium1py.pythonanywhere.com/" + language + "/catalogue/coders-at-work_207/" )

    yield browser
    print("\nquit browser..")
    browser.quit()

