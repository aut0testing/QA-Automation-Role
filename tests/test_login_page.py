import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password",
    [
        ("wronguser", "wrongpassword"),
        ("tomsmith", "wrongpassword"),
        ("wronguser", "SuperSecretPassword!"),
        ("", "SuperSecretPassword!"),
        ("tomsmith", ""),
        ("", ""),
    ]
)
def test_login_negative(page, username, password):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    assert login_page.error_message().is_visible()
    assert "invalid" in login_page.error_message_text().lower()
