import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

URL = "https://jqueryui.com/droppable/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(URL)
    sleep(2)
    d.switch_to.frame(0)
    yield d
    d.quit()

def test_drag_drop_positive(driver):
    action = ActionChains(driver)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    action.drag_and_drop(source, target).perform()
    sleep(2)

    assert target.text.strip() == "Dropped!"

def test_drag_drop_negative(driver):
    action = ActionChains(driver)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")

    action.drag_and_drop_by_offset(source, 280, 0).perform()
    sleep(2)

    assert target.text.strip() == "Drop here"
