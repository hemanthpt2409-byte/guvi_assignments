from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from pytest import fixtures

url = 'https://www.saucedemo.com/'

driver = webdriver.Edge()
driver.get(url)
time.sleep(5)

print('Title:',driver.title)
print('Current URL:',driver.current_url)
webelement_of_login_button = driver.find_element(By.ID,"user-name")
webelement_of_login_button.send_keys("standard_user")
webelement_of_password = driver.find_element(By.ID,"password")
webelement_of_password.send_keys("secret_sauce")
webelement_of_login_button= driver.find_element(By.ID,"login-button")
webelement_of_login_button.click()
print('Dashboard URL:',driver.current_url)

page_content=driver.page_source
file=open("Webpage_task_11.txt","w",encoding="utf-8")
file.write(page_content)
file.close()

#PyTest
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
