from pages.text_box import TextBox
from conftest import browser
from pages.form_page import FormPage
import time


def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('tester')
    time.sleep(2)
    text_box.full_name.clear()
    time.sleep(2)
    assert text_box.full_name.get_text() == ''


def state_and_city(browser):
    form_page = FormPage(browser)
    form_page.visit()

    form_page.state.click()
    form_page.state.send_keys('u')
    form_page.state.click()





