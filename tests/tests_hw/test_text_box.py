# Задача № 1
from pages.text_box import TextBox
from conftest import browser

def test_add_text(browser):
    text_box = TextBox(browser)
    text_box.visit()

    text_box.full_name.send_keys('tester')
    text_box.current_address.send_keys('St.Petersburg')
    text_box.btn_submit.click()
    assert text_box.full_name.get_text() == ''
    assert text_box.current_address.get_text() == ''

# Задача №