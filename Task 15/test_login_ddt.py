from pages.login_page import LoginPage
from utils.excel_reader import ExcelUtils



def test_login_ddt(driver):

    excel = ExcelUtils("testdata/login_data.xlsx")
    data = excel.get_data()

    page = LoginPage(driver)

    for username, password, row in data:

        driver.delete_all_cookies()   # reset session

        page.load()
        page.login(username, password)

        if page.verify_login():
            print("Login Passed")
        else:
            print("Login Failed")