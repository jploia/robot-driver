# this will include the code for the webscraper
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # p.firefox.launch(headless=False, slow_mo=50)
    browser = p.firefox.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()


