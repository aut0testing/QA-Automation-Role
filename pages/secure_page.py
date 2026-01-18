class SecurePage:
    PATH = "/secure"

    HEADER = "h2"
    PAGE_TEXT = "h4.subheader"
    POWERED_TEXT = "Powered by"
    POWERED_LINK = "a[href='http://elementalselenium.com/']"
    LOGOUT_BUTTON = "a.button.secondary.radius"
    FLASH_MESSAGE = "#flash"

    def __init__(self, page):
        self.page = page

    def is_opened(self):
        return self.page.url.endswith(self.PATH)

    def header(self):
        return self.page.locator(self.HEADER)

    def secure_header_text_is_visible(self):
        return self.page.locator(self.PAGE_TEXT, has_text="Welcome to the Secure Area").is_visible()

    def has_powered_by(self):
        return self.page.get_by_text(self.POWERED_TEXT).is_visible()

    def has_elemental_selenium_link(self):
        return self.page.locator(self.POWERED_LINK).is_visible()

    def elemental_link_text(self):
        return self.page.locator(self.POWERED_LINK).text_content()

    def logout_button(self):
        return self.page.locator(self.LOGOUT_BUTTON)

    def flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)

    def flash_message_text(self):
        return self.flash_message().text_content().strip()

    def logout(self):
        self.logout_button().click()
