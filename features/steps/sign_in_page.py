from behave import given, when
from selenium.webdriver.support import expected_conditions as EC




@given('Open reely signin page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Input valid credentials')
def input_valid_credentials(context):
    # context.driver.find_element(By.ID, "username").send_keys("lgodiva0808@gmail.com")
    # context.driver.find_element(By.ID, "password").send_keys("Ukraine#1")
    context.app.sign_in_page.enter_username()
    context.app.sign_in_page.enter_password()

@when('Click Continue button')
def click_continue_button(context):
    context.app.sign_in_page.click_continue_button()
    # context.driver.wait.until(EC.visibility_of_element_located(pass locator with password))





