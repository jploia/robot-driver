# this will include the code for the webscraper
from playwright.sync_api import sync_playwright, expect
from urllib.parse import urlparse

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
        page.get_by_role('button').click()
            # set timeout after TimeoutError

        # conduct search
        page.get_by_role('searchbox').click()
        page.keyboard.type(query, delay=100) # to mimic user typing
        page.keyboard.press('Enter', delay=100)

        # click first search result
        page.get_by_role('link').click()
        
        page.get_by_role('searchbox').click()

        page.keyboard.type(query, delay=100) # to mimic user typing
        # wait for results page
        # request = page.on('request')
        # request.all_headers()
        # with page.expect_request('*') as search:
            
        #     page.goto('https://wikipedia.org')
        # print(search.value.url)

        # scrape the data from the first page of results

        # results page
        print('Success!')


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
