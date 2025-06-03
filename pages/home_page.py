from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SIGNUP_LOGIN_BTN = (By.XPATH, "//a[text()=' Signup / Login']")
    HOME_BANNER = (By.XPATH, "//img[@alt='Website for automation practice']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_home_loaded(self):
        return self.is_visible(self.HOME_BANNER)

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BTN)
