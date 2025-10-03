import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service


def scrape_website(website):
    print("Launching firefox browser....")

    firefox_driver_path = r"D:\Projects\Web-Scraper\geckodriver.exe"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=Service(
        firefox_driver_path), options=options)

    try:
        driver.get(website)
        print("Website loaded....")
        html = driver.page_source

        return html
    finally:
        driver.quit()
