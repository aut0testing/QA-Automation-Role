from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = "/"
    GITHUB_BANNER = "img[alt='Fork me on GitHub']"
    INTERNAL_LINKS = "a[href^='/']"
    FORM_AUTH_LINK = "text=Form Authentication"
    EXPECTED_INTERNAL_LINKS_COUNT = 44

    def __init__(self, page, context):
        super().__init__(page, context)

    def open(self):
        self.goto(self.PATH)
        self.page.wait_for_load_state("networkidle")

    def go_to_login(self):
        self.page.click(self.FORM_AUTH_LINK)

    def get_title(self):
        return self.page.title()

    def has_github_banner(self):
        return self.page.locator(self.GITHUB_BANNER).is_visible()

    def get_internal_links_count(self):
        return self.page.locator(self.INTERNAL_LINKS).count()
