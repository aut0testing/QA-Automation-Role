from pages.main_page import MainPage

def test_main_page(page):
    main_page = MainPage(page)
    main_page.open()

    assert main_page.title_is_not_empty(), "Title страницы пустой!"
    assert main_page.has_github_banner()
    assert main_page.internal_links_count() == 44
