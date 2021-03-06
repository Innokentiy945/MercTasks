import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def set_up():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    yield driver
    driver.quit()
