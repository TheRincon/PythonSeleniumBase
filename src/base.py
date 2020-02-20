import unittest
from selenium import webdriver
from config import Config
from selenium.common.exceptions import NoSuchElementException
import selenium_setup as selenium_setter

class Base(unittest.TestCase):

    DRIVER = selenium_setter.chooser()

    def setUp(self):
        self.driver = self.DRIVER
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")

    def test_search_box(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
