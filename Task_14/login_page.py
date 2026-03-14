from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

        self.username = (By.XPATH, "//input[@placeholder='Enter your mail']")
        self.password = (By.XPATH, "//input[@placeholder='Enter your password ']")
        self.signin = (By.XPATH, "//form//button[@type='submit']")
        self.avatar = (By.CSS_SELECTOR, ".avatar-main-div")
        self.logout = (By.XPATH, "//div[text()='Log out")

    def load(self):
        self.driver.get("https://v2.zenclass.in/login")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.signin)).click()

    def verify_login_success(self):
        try:
            self.wait.until(EC.url_contains("dashboard"))
            return True
        except TimeoutException:
            return False

    def click_logout(self):

        wait = WebDriverWait(self.driver, 20)

        avatar = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".avatar-main-div"))
        )

        self.driver.execute_script("arguments[0].click();", avatar)

        logout_btn = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Log out']"))
        )

        self.driver.execute_script("arguments[0].click();", logout_btn)


    def verify_logout(self):
        self.wait.until(EC.url_contains("login"))
        return "login" in self.driver.current_url