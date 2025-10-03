import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
import time


def scrape_website(website):
    print("Launching firefox browser....")

    firefox_driver_path = "D:\Projects\Web-Scraper\geckodriver.exe"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=Service(
        firefox_driver_path), options=options)

    try:
        driver.get(website)
        print("Website loaded....")
        html = driver.page_source

        time.sleep(5)

        return html
    finally:
        driver.quit()
