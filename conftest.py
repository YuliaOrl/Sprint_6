import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1280,720')
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()