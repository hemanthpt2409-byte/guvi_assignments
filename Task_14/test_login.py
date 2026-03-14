from login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

# -------- Positive Login --------
def test_successful_login(driver):

    page = LoginPage(driver)
    page.load()

    page.login("hemanthpt2409@gmail.com", "Ragavendra@24")

    assert page.verify_login_success()

# -------- Negative Login --------
def test_unsuccessful_login(driver):

    page = LoginPage(driver)
    page.load()

    page.login("wrong_email", "wrong_password")

    assert not page.verify_login_success()


# -------- Validate Input Fields --------

def test_validate_input_fields(driver):
        page = LoginPage(driver)
        page.load()

        username = page.wait.until(
            EC.visibility_of_element_located(page.username)
        )

        password = page.wait.until(
            EC.visibility_of_element_located(page.password)
        )

        assert username.is_displayed()
        assert password.is_displayed()


# -------- Validate Submit Button --------
def test_validate_submit_button(driver):

    page = LoginPage(driver)
    page.load()

    assert driver.find_element(*page.signin).is_enabled()

# -------- Logout Test --------
def test_logout(driver):

    page = LoginPage(driver)
    page.load()

    page.login("hemanthpt2409@gmail.com", "Ragavendra@24")
    assert page.verify_login_success()

    page.click_logout()
    assert page.verify_logout()