from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")
        self.dashboard = (By.XPATH, "//h6[text()='Dashboard']")

    def load(self):
            self.driver.get("https://opensource-demo.orangehrmlive.com/")

            self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )

    def login(self, user, pwd):

        username_field = self.wait.until(
            EC.presence_of_element_located(self.username)
        )

        username_field.clear()
        username_field.send_keys(user)

        password_field = self.wait.until(
            EC.presence_of_element_located(self.password)
        )

        password_field.clear()
        password_field.send_keys(pwd)

        self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()


    def verify_login(self):
        try:
            self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )
            return True
        except:
            return False