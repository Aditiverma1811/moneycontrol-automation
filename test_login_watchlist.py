# NOTE:
# This UI test script is included for completeness.
# It was not executed in GitHub Codespaces due to missing Chrome/Firefox binaries.
# Only API tests were run and verified successfully.
import csv, pytest
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from utils import login, add_stock

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return uc.Chrome(options=options)

def test_watchlist():
    driver = get_driver()
    driver.maximize_window()

    login(driver, "aditikvarma@gmail.com", "Eddy@1811")

    driver.get("https://www.moneycontrol.com/watchlist/stocks")
    initial_count = len(driver.find_elements(By.XPATH, "//table//tr"))

    with open("stocks.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            add_stock(driver, row[0])

    final_count = len(driver.find_elements(By.XPATH, "//table//tr"))
    assert final_count == initial_count + 3

    driver.save_screenshot("Screenshots/watchlist.png")
    driver.quit()