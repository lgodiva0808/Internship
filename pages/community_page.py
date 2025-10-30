from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CommunityPage(Page):

    CONTACT_SUPPORT_BTN = (By.XPATH, "//a[text()='Contact Support']")


    def verify_community_page_opens(self):
        sleep(3)
        self.wait_until_url_contains('community')


    def verify_contact_support_button(self):
        sleep(2)
        result = self.find_elements(*self.CONTACT_SUPPORT_BTN)
        result = result[2].text
        assert result == 'Contact support', 'Contact support button not found'




