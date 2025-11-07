from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LandingPage(Page):
    SETTINGS = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')
    MENU_ICON = (By.CSS_SELECTOR, '[class*="new-market-menu-button _1"]')

    def click_settings(self):
        self.wait_until_clickable_click(*self.SETTINGS)
        sleep(3)

    def click_menu(self):
        self.wait_until_clickable_click(*self.MENU_ICON)

