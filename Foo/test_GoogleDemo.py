# Automation test for scripted in Python

# Author : Guruprasad R

# Importing Webdriver from the Selenium package
from selenium import webdriver
# Importing pytest package
import pytest

# Creating class TestGoogle
class TestGoogle():

    @pytest.fixture()
    def setup(self):
        # Initializing Webdriver and configuring path to executable
        self.driver = webdriver.Chrome(executable_path='/home/guppi/ChromeDriver76/chromedriver')
        # Maximizing browser window
        self.driver.maximize_window()
        # Every time method runs yield will be called and driver will be closed
        yield
        # Closing the driver
        self.driver.close()

    def test_googlePageTitle(self, setup):
        # Getting URL
        self.driver.get("https://www.google.com")
        # assertion of page tile - which is configured to 'FAIL' this method
        assert self.driver.title == "Google1"

    def test_gmailLinkClick(self, setup):
        self.driver.get("https://www.google.com")
        # Implicit wait for driver
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_class_name("gb_e").click()
        assert self.driver.title == "Gmail - Free Storage and Email from Google"
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_xpath("(.//a[contains(text(),'Sign in')])[2]").click()


