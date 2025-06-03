import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
from selenium import webdriver
from utils.config_loader import ConfigLoader
from utils.logger import setup_logger
import os

logger = setup_logger()


# Add CLI options
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment to run tests against")
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


# Make env and browser accessible in fixtures
@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# Load config per test session
@pytest.fixture(scope="session")
def config(env):
    return ConfigLoader(env).config


# WebDriver fixture
@pytest.fixture(scope="function")
def driver(browser, config, request):
    logger.info(f"Launching browser: {browser}")

    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if config.get("headless"):
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if config.get("headless"):
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.maximize_window()
    print(">>> Final URL to load:", config.get("base_url"))
    driver.get(config.get("base_url"))
    logger.info(f"Navigated to {config.get('base_url')}")

    yield driver

    if request.node.rep_call.failed:
        try:
            screenshot_path = os.path.join("reports", f"{request.node.name}.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test failed: screenshot saved to {screenshot_path}")
        except Exception as e:
            logger.error(f"Could not capture screenshot: {e}")

    driver.quit()
    logger.info("Browser closed.")


# Hook to detect test outcome
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
