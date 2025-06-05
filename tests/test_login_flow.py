import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -----------------------------
# Test Case 1: Open Login Page
# -----------------------------
@allure.feature("Login Page")
@allure.story("Validate Login Page Loads")
@pytest.mark.smoke
@pytest.mark.flaky(reruns=1)
def test_open_login_page(driver):
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']"))
    )
    heading = driver.find_element(By.XPATH, "//h2[text()='Login to your account']")
    assert heading.is_displayed()

# ---------------------------------------------------
# Test Case 2: Invalid Login Shows Error Message
# ---------------------------------------------------
@allure.feature("Login Page")
@allure.story("Invalid Login")
@pytest.mark.negative
def test_invalid_login(driver):
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "email").send_keys("invalid@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Your email or password is incorrect!']"))
    )
    assert error.is_displayed()

# ---------------------------------------------------
# Test Case 3: Verify Contact Us Page Loads
# ---------------------------------------------------
@allure.feature("Contact Page")
@allure.story("Contact Form Loads")
@pytest.mark.regression
def test_contact_us_page(driver):
    driver.find_element(By.LINK_TEXT, "Contact us").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Get In Touch']"))
    )
    assert "Get In Touch" in driver.page_source

# ---------------------------------------------------
# Test Case 4: Navigate to Products and Verify Title
# ---------------------------------------------------
@allure.feature("Product Page")
@allure.story("Product List Loads")
@pytest.mark.regression
def test_product_page_load(driver):
    driver.find_element(By.XPATH, "//a[@href='/products']").click()
    WebDriverWait(driver, 10).until(
        EC.title_contains("Automation Exercise - All Products")
    )
    assert "All Products" in driver.title

# ---------------------------------------------------
# Test Case 5: Verify Test Cases Menu Navigation
# ---------------------------------------------------
@allure.feature("Navigation")
@allure.story("Test Cases Menu")
@pytest.mark.regression
def test_test_cases_menu(driver):
    driver.find_element(By.LINK_TEXT, "Test Cases").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[text()='Test Cases']"))
    )
    assert "Test Cases" in driver.page_source

# ---------------------------------------------------
# Test Case 6: Verify Logo is Clickable and Home Redirects
# ---------------------------------------------------
@allure.feature("Header")
@allure.story("Logo Navigation")
@pytest.mark.ui
def test_logo_redirects_to_home(driver):
    driver.find_element(By.XPATH, "//a[@href='/products']").click()
    WebDriverWait(driver, 10).until(EC.title_contains("All Products"))
    driver.find_element(By.XPATH, "//div[@class='logo pull-left']/a").click()
    WebDriverWait(driver, 10).until(EC.title_is("Automation Exercise"))
    assert driver.title == "Automation Exercise"
