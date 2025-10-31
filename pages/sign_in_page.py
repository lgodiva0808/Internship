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
        sleep(1)
        self.input_text('lgodiva0808@gmail.com', *self.USERNAME_INPUT)
        sleep(1)

    def enter_password(self):
        sleep(1)
        self.input_text('Ukraine#1', *self.PASSWORD_INPUT)
        sleep(1)

    def click_continue_button(self):
        sleep(3)
        self.click(*self.CONTINUE_BUTTON)
        sleep(5) #wait for redirect after Login
