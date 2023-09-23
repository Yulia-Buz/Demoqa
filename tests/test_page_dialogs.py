from pages.modal_dialogs import ModalDialogs
from conftest import browser

def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.submenu_btns.check_count_elements(5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    browser.refresh()
    modal_dialogs.main_page_icon.click()
    modal_dialogs.back()
    browser.set_window_size(900, 400)
    modal_dialogs.forward()
    assert browser.current_url == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
