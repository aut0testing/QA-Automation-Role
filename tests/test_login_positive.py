from pages.login_page import LoginPage
from pages.secure_page import SecurePage

def test_login_positive(page):
    page_obj, context = page
    login_page = LoginPage(page_obj, context)
    secure_page = SecurePage(page_obj, context)
    
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_page.is_opened(), "Страница Secure Area не открылась"
    header = secure_page.get_header()
    assert header.is_visible(), "Заголовок страницы не отображается"
    assert secure_page.SECURE_AREA_TEXT in header.text_content(), f"Заголовок не содержит текст '{secure_page.SECURE_AREA_TEXT}'"
    assert secure_page.is_secure_header_text_visible(), "Текст 'Welcome to the Secure Area' не отображается"
    assert secure_page.has_powered_by(), "Текст 'Powered by' не отображается"
    assert secure_page.has_elemental_selenium_link(), "Ссылка на Elemental Selenium не отображается"
    assert secure_page.get_logout_button().is_visible(), "Кнопка выхода не отображается"
    assert secure_page.has_login_success_message(), f"Сообщение '{secure_page.LOGIN_SUCCESS_MESSAGE}' не найдено"

    secure_page.logout()
    assert page_obj.url.endswith("/login"), "После выхода не произошел переход на страницу логина"
    assert secure_page.has_logout_success_message(), f"Сообщение '{secure_page.LOGOUT_SUCCESS_MESSAGE}' не найдено"
