from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage, OrderPageLocators):
    
    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT))
        self.click_js(metro_input)
        
        metro_option = self.wait.until(EC.element_to_be_clickable(self.metro_option(metro)))
        self.click_js(metro_option)
        
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.DATE_INPUT))
    
   
    def _fill_date(self, date):
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
    
    def _fill_period(self, period):
        self.click(self.RENTAL_PERIOD)
        period_option = self.wait.until(EC.element_to_be_clickable(self.period_option(period)))
        self.click_js(period_option)
    
    def _fill_black_color(self):
        self.click(self.COLOR_BLACK)
    
    def _fill_grey_color(self):
        self.click(self.COLOR_GREY)
    
    def _fill_comment(self, comment):
        self.send_keys(self.COMMENT_INPUT, comment)
    
    def _submit_order(self):
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
  
    def fill_second_form_black_with_comment(self, date, period, comment):
        self._fill_date(date)
        self._fill_period(period)
        self._fill_black_color()
        self._fill_comment(comment)
        self._submit_order()
    
    def fill_second_form_black_without_comment(self, date, period):
        self._fill_date(date)
        self._fill_period(period)
        self._fill_black_color()
        self._submit_order()
    
    def fill_second_form_grey_with_comment(self, date, period, comment):
        self._fill_date(date)
        self._fill_period(period)
        self._fill_grey_color()
        self._fill_comment(comment)
        self._submit_order()
    
    def fill_second_form_grey_without_comment(self, date, period):
        self._fill_date(date)
        self._fill_period(period)
        self._fill_grey_color()
        self._submit_order()
    
    def confirm(self):
        self.click(self.CONFIRM_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))