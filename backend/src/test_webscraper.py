import unittest, webscraper, io, sys

URL = 'https://www.amazon.com/'

class TestWebscrapperMethods(unittest.TestCase):

    def test_valid_url_can_open_page(self):
        output = io.StringIO()
        sys.stdout = output # redirect stdout
        webscraper.open_page(URL)    
        sys.stdout = sys.__stdout__ # reset redirect
        output = output.getvalue()
        self.assertEqual(output, 'The page, Amazon.com, has successfully been opened.\n')

        


if __name__ == '__main__':
    unittest.main()