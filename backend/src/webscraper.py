# this will include the code for the webscraper
from playwright.sync_api import sync_playwright

def open_page(url: str) -> None:
    '''Opens the provided url and prints a success message if successful,
    otherwise nothing is printed'''
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(url)

        # error check if the page has been opened

        print(f'The page, {page.title()}, has successfully been opened.')
        browser.close()

# for testing purposes only
# if __name__ == '__main__':
#     open_page('https://amazon.com/')
