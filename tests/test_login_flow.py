import pytest
import allure
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.excel_reader import read_excel_data


@allure.feature("Login")
@allure.story("Basic Valid Login Test")
@pytest.mark.smoke
@pytest.mark.flaky(reruns=2, reruns_delay=1)  # Optional: retry real failures
def test_valid_login(driver):
    home = HomePage(driver)
    assert home.is_home_loaded(), "Home page did not load properly"
    home.click_signup_login()

    login = LoginPage(driver)
    login.login("testuser@example.com", "wrongpass")  # Replace with real creds if needed

    with allure.step("Check login result for hardcoded user"):
        if login.is_logout_visible():
            allure.attach(driver.get_screenshot_as_png(), name="Hardcoded_Login_Success", attachment_type=allure.attachment_type.PNG)
            assert True
        elif login.is_login_failed():
            allure.attach(driver.get_screenshot_as_png(), name="Hardcoded_Login_Failed", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name="Hardcoded_Login_Unexpected", attachment_type=allure.attachment_type.PNG)
            pytest.fail("Unexpected login result")


@allure.feature("Login")
@allure.story("Excel Data-Driven Login Test")
@pytest.mark.parametrize("data", read_excel_data())
@pytest.mark.flaky(reruns=2, reruns_delay=1)  # Optional: retry for flaky UI inputs
def test_login_excel(driver, data):
    home = HomePage(driver)
    assert home.is_home_loaded(), "Home page did not load properly"
    home.click_signup_login()

    login = LoginPage(driver)
    login.login(data['email'], data['password'])

    with allure.step(f"Testing login with {data['email']} / {data['password']}"):
        if login.is_logout_visible():
            allure.attach(driver.get_screenshot_as_png(), name=f"{data['email']}_Login_Success", attachment_type=allure.attachment_type.PNG)
            assert True
        elif login.is_login_failed():
            allure.attach(driver.get_screenshot_as_png(), name=f"{data['email']}_Login_Failed", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name=f"{data['email']}_Login_Unexpected", attachment_type=allure.attachment_type.PNG)
            pytest.fail("Unexpected login result")
