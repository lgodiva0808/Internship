from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SettingsPage(Page):
    COMMUNITY_OPT = (By. CSS_SELECTOR, 'a.page-setting-block.w-inline-block[href="/community"]')

    def click_community(self):
        self.scroll_to_element(*self.COMMUNITY_OPT)
        self.wait_until_clickable_click(*self.COMMUNITY_OPT)
        sleep(2)
