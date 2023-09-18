from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_please = WebElement(driver, #app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text)
        self.text_elements = WebElement(driver, 'div.playground-header > div')

