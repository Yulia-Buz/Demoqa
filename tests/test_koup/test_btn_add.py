from conftest import browser
from pages.herokuapp_page import HerokuappPage
from pages.Heroku_add_remove import AddRemove

def test_add_remove_elements(browser):
    herokuapp_page = HerokuappPage(browser)
    herokuapp_page.visit()

    assert herokuapp_page.add_remove_element.get_text() == "Add/Remove Elements"
    herokuapp_page.add_remove_element.click()

    add_remove = AddRemove(browser)
    assert add_remove.equal_url()
    assert add_remove.add_element_btn.get_text() == "Add Element"
    assert add_remove.add_element_btn.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        add_remove.add_element_btn.click()

    assert add_remove.del_btn.check_count_elements(4)

    for element in add_remove.del_btn.find_elements():
        assert element.text == 'Delete'

    while add_remove.del_btn.exist():
        add_remove.del_btn.click()

    assert not add_remove.del_btn.exist()



