import pytest

from selenium import webdriver

from data.routes import Routes
from pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Routes.main_page)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)
