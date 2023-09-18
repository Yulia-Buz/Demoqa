from conftest import browser
from elements_page import ElementsPage
def test_page_elements(browser):

    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'

