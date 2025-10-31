from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class LandingPage(Page):
    SETTINGS = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')

    def click_settings(self):
        sleep(10)
        print(">>> Trying to click Settings button (JS method)...")
        element = self.find_element(*self.SETTINGS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        sleep(1)
        self.driver.execute_script("arguments[0].click();", element)
        print(">>> Clicked Settings via JavaScript.")
        sleep(5)

