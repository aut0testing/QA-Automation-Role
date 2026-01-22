from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/login"

    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"
    
    INVALID_CREDENTIALS_TEXT = "invalid"

    def __init__(self, page, context):
        super().__init__(page, context)

    def open(self):
        self.goto(self.PATH)

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def error_message(self):
        return self.page.locator(self.FLASH_MESSAGE)

    def get_error_message_text(self):
        return self.error_message().text_content().strip()
    
    def is_error_message_visible(self):
        self.error_message().wait_for(state="visible")
        return self.error_message().is_visible()
    
    def has_invalid_credentials_message(self):
        return self.INVALID_CREDENTIALS_TEXT in self.get_error_message_text().lower()