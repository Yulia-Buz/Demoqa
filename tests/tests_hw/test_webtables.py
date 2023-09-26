from conftest import browser
from pages.webtables import WebTables
import time

def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()

    assert web_tables.add_btn.exist()
    web_tables.add_btn.click()
    assert web_tables.reg_form.exist()
    assert not web_tables.submit_btn.click()
    web_tables.first_name.send_keys('tester')
    web_tables.last_name.send_keys('testerov')
    web_tables.email.send_keys('tt@ttt.tt')
    web_tables.age.send_keys('33')
    web_tables.salary.send_keys('10000')
    web_tables.department.send_keys('QA_Team')
    web_tables.submit_btn.click()
    time.sleep(2)
    assert not web_tables.reg_form.exist()
    assert not web_tables.row.get_text() == ''

    web_tables.pencil.click()
    time.sleep(2)
    assert web_tables.reg_form.exist() #не догадалась пока как проверить наличие данных в форме
    web_tables.first_name.clear()
    web_tables.first_name.send_keys('testers')
    web_tables.submit_btn.click()
    time.sleep(2)
    assert web_tables.first_name_text.get_text() == "testers"
    web_tables.delete_btn.click()
    assert not web_tables.reg_form.exist()

