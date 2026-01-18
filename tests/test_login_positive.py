from pages.login_page import LoginPage
from pages.secure_page import SecurePage

def test_login_positive(page):
    login_page = LoginPage(page)
    secure_page = SecurePage(page)
    
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_page.is_opened()
    assert secure_page.header().is_visible()
    assert "Secure Area" in secure_page.header().text_content()
    assert secure_page.secure_header_text_is_visible()
    assert secure_page.has_powered_by()
    assert secure_page.has_elemental_selenium_link()
    assert secure_page.logout_button().is_visible()
    assert "You logged into a secure area!" in secure_page.flash_message_text()

    secure_page.logout()
    assert page.url.endswith("/login")
    assert "You logged out of the secure area!" in secure_page.flash_message_text()
