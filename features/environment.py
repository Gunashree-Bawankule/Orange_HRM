from behave import *
from playwright.sync_api import sync_playwright
from behave import use_fixture
import os
from dotenv import load_dotenv
import allure

load_dotenv()


def before_all(context):
    context.browser = os.getenv("BROWSER", "chrome")
    context.url = os.getenv(
        "URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )
    print(context.url, context.browser)


def setup_browser(context, playwright):
    if context.browser == "chrome":
        browser = playwright.chromium.launch(headless=False, slow_mo=200)
    else:
        raise ValueError("Unknown browser type")

    context.browser_context = browser.new_context(
        ignore_https_errors=True,
    )
    context.page = context.browser_context.new_page()
    return browser


@fixture
def setup_playwright(context):
    playwright = sync_playwright().start()
    browser = setup_browser(context, playwright)
    yield context.page
    browser.close()
    playwright.stop()


def before_scenario(context, scenario):
    use_fixture(setup_playwright, context)
    context.page.goto(context.url)
