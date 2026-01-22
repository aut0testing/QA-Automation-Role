import pytest
from pages.main_page import MainPage
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
    page_obj, context = page
    main_page = MainPage(page_obj, context)
    login_page = LoginPage(page_obj, context)
    
    main_page.open()
    main_page.go_to_login()
    login_page.login(username, password)

    assert login_page.is_error_message_visible(), "Сообщение об ошибке не отображается"
    assert login_page.has_invalid_credentials_message(), f"Текст сообщения об ошибке не содержит '{login_page.INVALID_CREDENTIALS_TEXT}'"
