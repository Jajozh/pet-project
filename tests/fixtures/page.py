import pytest
from playwright.sync_api import sync_playwright
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="function")
def browser():
    headless = os.getenv("HEADLESS", "True").lower() == "true"
    slow_mo = int(os.getenv("SLOW_MO", "0"))  # Читаем из .env, по умолчанию 0 (без замедления)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()
