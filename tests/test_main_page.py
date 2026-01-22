from pages.main_page import MainPage

def test_main_page(page):
    page_obj, context = page
    main_page = MainPage(page_obj, context)
    main_page.open()

    title = main_page.get_title()
    assert title, "Title страницы пустой!"
    assert main_page.has_github_banner(), "GitHub баннер не отображается"
    links_count = main_page.get_internal_links_count()
    assert links_count == main_page.EXPECTED_INTERNAL_LINKS_COUNT, f"Ожидалось {main_page.EXPECTED_INTERNAL_LINKS_COUNT} внутренних ссылок, получено {links_count}"
