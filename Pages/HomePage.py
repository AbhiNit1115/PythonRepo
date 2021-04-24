from Locators.LoginAndHomePageLocators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_id = Locators.welcome_id
        self.logout_link_text = Locators.logout_link_text

    def click_welcome_link(self):
        wlcome = self.driver.find_element_by_id(self.welcome_id)
        wlcome.click()

    def click_logout_link(self):
        lgout = self.driver.find_element_by_link_text(self.logout_link_text)
        lgout.click()
