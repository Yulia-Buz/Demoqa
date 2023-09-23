from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

def test_size(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

def test_visible_nav_bar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert not elements_page.nav_bar.visible()
    browser.set_window_size(767, 1000)
    assert elements_page.nav.bar.visible()