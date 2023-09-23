from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from pages.form_page import FormPage
from conftest import browser
import time

def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)

    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)


    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('St.Petersburg, Russia')

# Задача №3 и ДЗ №9, пока не дается
#     form_page.refresh()
#     form_page.state.click()
#     time.sleep(1)
#     form_page.uttar.click_force()
#     time.sleep(1)
#     form_page.city.click()
#     time.sleep(1)
#     form_page.agra.click()


