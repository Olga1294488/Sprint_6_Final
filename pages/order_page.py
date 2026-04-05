from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage, OrderPageLocators):
    
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT))
        self.click_js(metro_input)
        
        metro_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//li[contains(text(), '{metro}')]")))
        self.click_js(metro_option)
        
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.DATE_INPUT))
    
    def fill_second_form_black_with_comment(self, date, period, comment):
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
        
        self.click(self.RENTAL_PERIOD)
        
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{period}')]")))
        self.click_js(period_option)
        
        self.click(self.COLOR_BLACK)
        self.send_keys(self.COMMENT_INPUT, comment)
        
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
    def fill_second_form_black_without_comment(self, date, period):
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
        
        self.click(self.RENTAL_PERIOD)
        
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{period}')]")))
        self.click_js(period_option)
        
        self.click(self.COLOR_BLACK)
        
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
    def fill_second_form_grey_with_comment(self, date, period, comment):
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
        
        self.click(self.RENTAL_PERIOD)
        
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{period}')]")))
        self.click_js(period_option)
        
        self.click(self.COLOR_GREY)
        self.send_keys(self.COMMENT_INPUT, comment)
        
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
    def fill_second_form_grey_without_comment(self, date, period):
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
        
        self.click(self.RENTAL_PERIOD)
        
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{period}')]")))
        self.click_js(period_option)
        
        self.click(self.COLOR_GREY)
        
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
    def confirm(self):
        self.click(self.CONFIRM_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))