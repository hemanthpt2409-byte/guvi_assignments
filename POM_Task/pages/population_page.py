from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WorldPopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

    population_xpath = "//span[contains(@class,'counter-number')]"

    def load_page(self):
        self.driver.get(self.url)

    def get_population(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.population_xpath))
        )
        return element.text