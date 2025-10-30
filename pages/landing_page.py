from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LandingPage(Page):
    SETTINGS = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')

    def click_settings(self):
        sleep(10)
        self.click(*self.SETTINGS)
