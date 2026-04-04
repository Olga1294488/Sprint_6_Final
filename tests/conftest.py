import pytest
import sys
import os
from selenium import webdriver

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()