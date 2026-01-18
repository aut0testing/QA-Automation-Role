class MainPage:
    PATH = "/"
    GITHUB_BANNER = "img[alt='Fork me on GitHub']"
    INTERNAL_LINKS = "a[href^='/']"
    FORM_AUTH_LINK = "text=Form Authentication"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(f"{self.page.base_url}{self.PATH}")

    def go_to_login(self):
        self.page.click(self.FORM_AUTH_LINK)

    def title(self):
        return self.page.title()

    def title_is_not_empty(self):
        return bool(self.page.title())

    def has_github_banner(self):
        return self.page.locator(self.GITHUB_BANNER).is_visible()

    def internal_links_count(self):
        return self.page.locator(self.INTERNAL_LINKS).count()
