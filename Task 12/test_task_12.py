import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.guvi.in/")
time.sleep(5)   # wait for page to load

# ---- Base element (red-underlined header item) ----
label = "Login"   # change to Courses / Practice / Resources / Sign up

base_xpath = f"//*[self::a or self::button][normalize-space()='{label}']"

base_el = driver.find_element(By.XPATH, base_xpath)
print("Base element text:", base_el.text)

# 1) Find parent element
parent_el = driver.find_element(By.XPATH, base_xpath + "/parent::*")
print("Parent tag:", parent_el.tag_name)

# 2) Find first child of the parent
first_child = driver.find_element(By.XPATH, base_xpath + "/parent::*/*[1]")
print("First child tag:", first_child.tag_name)

# 3) Locate second sibling (if any)
second_siblings = driver.find_elements(
    By.XPATH, base_xpath + "/following-sibling::*[2]"
)

if second_siblings:
    print("Second sibling text:", second_siblings[0].text)
else:
    print("No second sibling found")

# 4) Select parent element of an element having attribute 'href'
href_parents = driver.find_elements(
    By.XPATH, f"(//*[@href][normalize-space()='{label}'])/parent::*"
)

if href_parents:
    print("Href parent tag:", href_parents[0].tag_name)
else:
    print("Element with href not found (might be a button)")

# ---- Axes ----

# A) All ancestor elements
ancestors = driver.find_elements(By.XPATH, base_xpath + "/ancestor::*")
print("Ancestors count:", len(ancestors))

# B) All following siblings
following_siblings = driver.find_elements(By.XPATH, base_xpath + "/following-sibling::*")
print("Following siblings count:", len(following_siblings))

# C) All preceding elements
preceding_elements = driver.find_elements(By.XPATH, base_xpath + "/preceding::*")
print("Preceding elements count:", len(preceding_elements))

time.sleep(3)
driver.quit()