from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.add_btn = WebElement(driver, '#addNewRecordButton')
        self.reg_form = WebElement(driver, '#registration-form-modal')
        self.submit_btn = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.row = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]', 'xpath')
        self.pencil = WebElement(driver, '#edit-record-4 > svg')
        self.first_name_table = WebElement(driver, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[1]','xpath')
        self.delete_btn = WebElement(driver, '#delete-record-4 > svg > path')


