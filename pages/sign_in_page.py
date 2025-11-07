from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    USERNAME_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-name="Password"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@class="login-button w-button"]')


    def open_sign_in_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(2) # headless: allow page to Load fully

    def enter_username(self):
        self.wait_until_element_appear(*self.USERNAME_INPUT)
        self.input_text('lgodiva0808@gmail.com', *self.USERNAME_INPUT)

    def enter_password(self):
        self.wait_until_element_appear(*self.PASSWORD_INPUT)
        self.input_text('Ukraine#1', *self.PASSWORD_INPUT)

    def click_continue_button(self):
        self.wait_until_clickable_click(*self.CONTINUE_BUTTON)
        sleep(3) #wait for redirect after Login
