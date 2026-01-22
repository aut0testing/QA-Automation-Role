from pages.base_page import BasePage


class SecurePage(BasePage):
    PATH = "/secure"

    HEADER = "h2"
    PAGE_TEXT = "h4.subheader"
    POWERED_TEXT = "Powered by"
    POWERED_LINK = "a[href='http://elementalselenium.com/']"
    LOGOUT_BUTTON = "a.button.secondary.radius"
    FLASH_MESSAGE = "#flash"
    
    SECURE_AREA_TEXT = "Secure Area"
    WELCOME_TEXT = "Welcome to the Secure Area"
    LOGIN_SUCCESS_MESSAGE = "You logged into a secure area!"
    LOGOUT_SUCCESS_MESSAGE = "You logged out of the secure area!"

    def __init__(self, page, context):
        super().__init__(page, context)

    def is_opened(self):
        return self.page.url.endswith(self.PATH)

    def get_header(self):
        return self.page.locator(self.HEADER)

    def is_secure_header_text_visible(self):
        return self.page.locator(self.PAGE_TEXT, has_text=self.WELCOME_TEXT).is_visible()

    def has_powered_by(self):
        return self.page.get_by_text(self.POWERED_TEXT).is_visible()

    def has_elemental_selenium_link(self):
        return self.page.locator(self.POWERED_LINK).is_visible()

    def get_logout_button(self):
        return self.page.locator(self.LOGOUT_BUTTON)

    def get_flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)

    def get_flash_message_text(self):
        return self.get_flash_message().text_content().strip()
    
    def wait_for_flash_message(self):
        self.get_flash_message().wait_for(state="visible")
    
    def has_login_success_message(self):
        self.wait_for_flash_message()
        return self.LOGIN_SUCCESS_MESSAGE in self.get_flash_message_text()
    
    def has_logout_success_message(self):
        self.wait_for_flash_message()
        return self.LOGOUT_SUCCESS_MESSAGE in self.get_flash_message_text()

    def logout(self):
        self.get_logout_button().click()
