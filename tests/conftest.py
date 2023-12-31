import os

import pytest
from selene import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
import dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.join(BASE_DIR, "resources")


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()


"""
def pytest_addoption(parser):
    
    parser.addoption(
        "--browser",
        help="Браузер для запуска тестов",
        choices=["firefox", "chrome"],
        default="chrome"
    )
    parser.addoption(
        "--browser_version",
        help="Версия браузера",
        default="100.0"
    )
"""


@pytest.fixture(scope="function")
def setup_browser(request):
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://4596d0720ffc4b92d7fd6f5ba399273c71eac54c",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Arxiv Mobile",
            "buildName": "arxiv-mobile-build-1",
            "sessionName": "arxiv first_test",

            # Set your access credentials
            "userName": os.getenv("BROWSERSTACK_LOGIN"),
            "accessKey": os.getenv("BROWSERSTACK_PASSWORD")
        }
    })

    # Initialize the remote Webdriver using BrowserStack remote URL
    # and options defined above
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    browser.config.driver = driver

    yield browser

    browser.quit()
