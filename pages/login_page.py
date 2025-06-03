from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'incorrect')]")
    LOGOUT_LINK = (By.XPATH, "//a[text()=' Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.type(self.LOGIN_EMAIL, email)
        self.type(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_failed(self):
        return self.is_visible(self.LOGIN_ERROR)

    def is_logout_visible(self):
        return self.is_visible(self.LOGOUT_LINK)
