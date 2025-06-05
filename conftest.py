# conftest.py (place this in your root project dir)
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import os
import sys
import pytest
from selenium import webdriver
from utils.config_loader import ConfigLoader
from utils.logger import setup_logger

logger = setup_logger()
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests against")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def config(env):
    # ✅ Fixed usage of ConfigLoader constructor
    return ConfigLoader(env).config

@pytest.fixture(scope="function")
def driver(browser, config, request):
    logger.info(f"Launching browser: {browser}")
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(config.get("base_url"))
    logger.info(f"Navigated to {config.get('base_url')}")

    yield driver

    if request.node.rep_call.failed:
        os.makedirs("Screenshots", exist_ok=True)
        path = os.path.join("Screenshots", f"{request.node.name}.png")
        driver.save_screenshot(path)
        logger.error(f"Test failed. Screenshot saved to {path}")

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
