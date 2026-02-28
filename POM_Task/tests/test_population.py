from pages.population_page import WorldPopulationPage


def test_world_population(driver):

    page = WorldPopulationPage(driver)
    page.load_page()

    print("Press CTRL+C to stop\n")

    try:
        while True:
            population = page.get_population()
            print("Current World Population:", population)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped by user")