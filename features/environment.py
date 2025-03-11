#from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright
#
# @fixture
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

def before_all(context):

    # context.browser = sync_playwright().chromium.launch(headless=False)
    # context.page = context.browser.new_page()

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page=context.browser.new_page()
    # context.enter_credentials(context.username, context.password)



def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    context.page.close()
    pass

def after_all(context):
    context.page.close()
    pass