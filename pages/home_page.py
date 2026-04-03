from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage, HomePageLocators):
    
    def click_order_top(self):
        button = self.find_element(self.ORDER_BUTTON_TOP)
        self.click_js(button)
    
    def click_question(self, index):
        questions = self.find_elements(self.ACCORDION_BUTTON)
        self.click_js(questions[index])
        self.wait.until(EC.visibility_of_element_located(self.VISIBLE_ACCORDION_PANEL))
    
    def get_answer_text(self):
        return self.get_text(self.VISIBLE_ACCORDION_PANEL)
    
    def click_scooter_logo(self):
        self.click_js(self.find_element(self.SCOOTER_LOGO))
    
    def get_current_url(self):
        return self.driver.current_url