from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when('Click Settings option')
def click_settings(context):
    context.app.landing_page.click_settings()



    