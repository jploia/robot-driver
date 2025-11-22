import unittest, webscraper, io, sys

URL = 'https://www.amazon.com/'

class TestWebscrapperMethods(unittest.TestCase):

    def test_valid_url_can_open_page(self):
        output = io.StringIO()
        sys.stdout = output # redirect stdout
        webscraper._open_page(URL)    
        sys.stdout = sys.__stdout__ # reset redirect
        output = output.getvalue()
        self.assertEqual(output, 'The page, Amazon.com, has successfully been opened.\n')

    def test_invalid_url_raises_exception(self):
        with self.assertRaises(Exception):
            webscraper._open_page(f'https://www.asjmazon.coon')    

    def test_valid_search_provides_a_title(self):
        pass

    def test_invalid_search_raises_exception(self):
        pass
        


if __name__ == '__main__':
    unittest.main()