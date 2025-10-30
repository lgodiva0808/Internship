from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Community page opens')
def community_page_opens(context):
    context.app.community_page.verify_community_page_opens()


@then('Verify Contact support button is available')
def verify_contact_support_button(context):
    context.app.community_page.verify_contact_support_button()
    

    
