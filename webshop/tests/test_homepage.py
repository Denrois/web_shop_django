import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Turn on browser in headless mode
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_homepage_displays_products(browser):
    browser.get("http://127.0.0.1:8000/")
    assert "Product List" in browser.page_source


def test_all_products_are_listed(browser):
    browser.get("http://127.0.0.1:8000/")
    assert "Product_1" in browser.page_source
    assert "Product_2" in browser.page_source