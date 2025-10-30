from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.landing_page import LandingPage 
from pages.settings_page import SettingsPage
from pages.community_page import CommunityPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.landing_page = LandingPage(driver)
        self.settings_page = SettingsPage(driver)
        self.community_page = CommunityPage(driver)
    
    