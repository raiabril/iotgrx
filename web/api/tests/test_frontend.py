import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .config import Config


class TestNavigateLanding(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        firefox_profile = webdriver.FirefoxProfile(self.config.FIREFOX_PROFILE_PATH)
        self.driver = webdriver.Firefox(
            executable_path=self.config.WEBDRIVER_PATH,
            firefox_profile=firefox_profile)

    # def testLoadPage(self):
    #     self.driver.get(self.config.FRONTEND_URL)
    #     self.assertTrue(self.driver.find_element_by_tag_name('title'))

    # def tearDown(self):
    #     self.driver.quit()
