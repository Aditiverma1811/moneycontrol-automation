from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get("https://www.moneycontrol.com/")
    driver.find_element(By.LINK_TEXT, "Login").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    ).send_keys(username)
    driver.find_element(By.ID, "pwd").send_keys(password)
    driver.find_element(By.ID, "loginbtn").click()

def add_stock(driver, stock_name):
    driver.get("https://www.moneycontrol.com/watchlist/stocks")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search_str"))
    )
    search_box.clear()
    search_box.send_keys(stock_name)
    driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()