class LoginPage:
    PATH = "/login"

    #USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{self.page.base_url}{self.PATH}")

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def error_message(self):
        return self.page.locator(self.FLASH_MESSAGE)

    def error_message_text(self):
        return self.error_message().text_content().strip()
