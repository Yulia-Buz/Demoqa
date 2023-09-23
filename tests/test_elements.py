from conftest import browser
from pages.elements_page import ElementsPage
from pages.check_box import CheckBox

def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(count=9)


def test_count_checkbox(browser):
    check_page = CheckBox(browser)

    check_page.visit()
    assert check_page.checkbox.check_count_elements(1)
    check_page.btn_expand_all.click()
    assert check_page.checkbox.check_count_elements(17)
    browser.refresh()
    assert check_page.checkbox.check_count_elements(1)

