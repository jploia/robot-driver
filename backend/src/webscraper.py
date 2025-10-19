# this will include the code for the webscraper
from playwright.sync_api import sync_playwright, expect

# primary function containing the functionality of the program
def search_item(url: str, query: str) -> str:
    '''Returns a string of the title of the first result from the given 
    query and url'''
    # open page -- remove function to stay within the event loop?
    # browser, page = _open_page(url)
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=50) # headless for testing purposes
        page = browser.new_page()
        try:
            page.goto(url)
        except:
            raise Exception(f'Sorry, the page associated with {url} does not exist.')

        print(f'The page, {page.title()}, has successfully been opened.')
    
        # bypass continue shopping button
        page.get_by_role("button").click()

        # conduct search
        # search bar ID: id="nav-search-bar-form"
        # page.locator('twotabsearchtextbox').press('Enter')
        # page.get_by_role("text").press('h')
        page.get_by_role("searchbox").click()
        # page.get_by_role("twotabsearchtextbox").dispatch_event('click')
        
        # page.locator('#nav-search-bar-form').press_sequentially('banana')
        
        print('yay')

        # close browser
        browser.close()


def _open_page(url: str) -> '(playwright.Browser, playwright.page)':
    '''Opens the provided url and prints a success message if successful,
    otherwise nothing is printed. Returns the browser.'''
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        try:
            page.goto(url)
        except:
            raise Exception(f'Sorry, the page associated with {url} does not exist.')

        print(f'The page, {page.title()}, has successfully been opened.')
        return browser, page

# for testing purposes only
if __name__ == '__main__':
    # _open_page('https://amazon.com/')
    search_item('https://amazon.com', 'bananas')
