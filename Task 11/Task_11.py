import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://www.guvi.in/"
SIGNIN_URL = "https://www.guvi.in/sign-in/"

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_guvi(driver):
    driver.get(BASE_URL)
    time.sleep(3)
    assert "GUVI" in driver.title

def test_login_navigation(driver):
    driver.get(BASE_URL)
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='login-btn']").click()
    time.sleep(3)
    assert "sign-in" in driver.current_url.lower()

def test_login_fields_displayed(driver):
    driver.get(SIGNIN_URL)
    time.sleep(3)
    username = driver.find_element(By.XPATH, "//input[@type='email']")
    password = driver.find_element(By.XPATH, "//input[@type='password']")
    assert username.is_displayed() and username.is_enabled()
    assert password.is_displayed() and password.is_enabled()

def test_invalid_login(driver):
    driver.get(SIGNIN_URL)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("wrong@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("wrong123")
    driver.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(3)
    assert "sign-in" in driver.current_url.lower()