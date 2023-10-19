import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose language: en, es, ru...")
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    # if browser_name == "chrome":
    print("\nЗапуск браузер Chrome для теста...")
    options = OptionsChrome()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    # else:
    #     raise pytest.UsageError("--browser_name должно быть chrome")
    yield browser
    print("\nЗакрыть браузер...")
    browser.quit()