import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()


def test_title_and_homepage_url(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    time.sleep(2)

    # Print and verify Title
    print("Title:", driver.title)
    assert "Swag Labs" in driver.title

    # Print and verify current homepage URL
    print("Current URL:", driver.current_url)
    assert "saucedemo.com" in driver.current_url


def test_positive_login_dashboard_url(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    time.sleep(2)

    # Elements (from your code)
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Positive credentials (Saucedemo gives for practice)
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    time.sleep(2)

    # Dashboard URL
    dashboard_url = driver.current_url
    print("Dashboard URL:", dashboard_url)

    assert "inventory" in dashboard_url   # Successful login leads to /inventory.html

def test_negative_login(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    time.sleep(2)

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Wrong credentials
    username.send_keys("wrong_user")
    password.send_keys("wrong_password")
    login_button.click()
    time.sleep(2)

    # Check that login FAILED (URL should NOT be inventory)
    assert "inventory" not in driver.current_url
    print("Negative Login Test: URL =", driver.current_url)

def test_save_page_content(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    time.sleep(2)

    page_content = driver.page_source

    file_path = Path("Webpage_task_11.txt")
    file_path.write_text(page_content, encoding="utf-8")

    print("Page saved at:", file_path)
    assert file_path.exists()