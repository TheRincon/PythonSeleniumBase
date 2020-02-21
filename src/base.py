import unittest
from selenium import webdriver
from config import Config
import tools as tl
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import selenium_setup as selenium_setter

class Base(unittest.TestCase):

    DRIVER = selenium_setter.chooser()

    def setUp(self):
        self.driver = self.DRIVER
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

class SampleTest(Base):
    def test_search_box(self):
        self.driver.get("http://www.google.com/")
        self.assertTrue(tl.is_element_present(self.driver, By.NAME, "q"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
