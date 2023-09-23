from conftest import browser
from elements_page import ElementsPage
from pages.demoqa import DemoQa
def test_page_elements(browser):

    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()