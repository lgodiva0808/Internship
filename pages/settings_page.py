from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SettingsPage(Page):
    COMMUNITY_OPT = (By. CSS_SELECTOR, 'a.page-setting-block.w-inline-block[href="/community"]')

    def click_community(self):
        sleep(5)
        print(">>> Trying to click Community button (JS method)...")
        element = self.find_element(*self.COMMUNITY_OPT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        print(">>> Clicked Community via JavaScript.")
        sleep(5)
