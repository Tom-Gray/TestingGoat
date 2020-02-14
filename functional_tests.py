from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #open homepage
        self.browser.get('http://localhost:8000')

        #check page title and header for todo lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')