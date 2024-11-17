from pages.MenuPage import MenuPage


def test_menu_items(driver):
    menu_page = MenuPage(driver)
    menu_page.open()
    menu_page.click_menu_item('Tablets')
    assert menu_page.get_page_heading_text() == 'Tablets'

