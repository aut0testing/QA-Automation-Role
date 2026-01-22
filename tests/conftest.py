import sys
import os
import pytest
from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://the-internet.herokuapp.com",
        help="Base URL для тестов"
    )

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def page(base_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.base_url = base_url
        page = context.new_page()
        yield page, context
        context.close()
        browser.close()
