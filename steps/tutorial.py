from behave import *
from selenium.webdriver.chrome.options import Options
from PageObject.MainPage import GooglePage
from selenium import webdriver

chrome_options = Options()

@given('open "{Device}" website with "{Url}"')
def step_impl(context,Device, Url):
    try:
        chrome_options.add_experimental_option("mobileEmulation", context.DeviceSetting.__getattribute__(Device))
    except:
        print("Cannot find any Device")
    context.browser = GooglePage(webdriver.Chrome(chrome_options = chrome_options))
    context.browser.open(Url)

@when('click search text with "{searchValue}"')
def step_impl(context,searchValue):
    context.browser.SearchValue(searchValue)
    assert context.failed is False

#@when('click search text with 2 {searchValue}')
#def step_impl(context,searchValue):
#    context.browser.SearchValue(searchValue)

@then('Close')
def step_impl(context):
    print("close")