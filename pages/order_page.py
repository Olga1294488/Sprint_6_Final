from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class OrderPage(BasePage, OrderPageLocators):
    
    def fill_first_form(self, name, surname, address, metro, phone):
        # Заполняем поля
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        
        # Клик по полю метро
        metro_input = self.wait.until(EC.element_to_be_clickable(self.METRO_INPUT))
        self.click_js(metro_input)
        
        # Выбор станции метро
        metro_locator = self.metro_option(metro)
        metro_option = self.wait.until(EC.element_to_be_clickable(metro_locator))
        self.click_js(metro_option)
        
        # Телефон и далее
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)
        
        # Ждём появления второй формы
        self.wait.until(EC.presence_of_element_located(self.DATE_INPUT))
    
    def fill_second_form(self, date, period, color, comment):
        # Дата
        self.send_keys(self.DATE_INPUT, date)
        self.find_element(self.DATE_INPUT).send_keys("\n")
        
        # Срок аренды
        self.click(self.RENTAL_PERIOD)
        period_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//div[contains(text(), '{period}')]")))
        self.click_js(period_option)
        
        # Цвет
        if color == "black":
            self.click(self.COLOR_BLACK)
        else:
            self.click(self.COLOR_GREY)
        
        # Комментарий
        if comment:
            self.send_keys(self.COMMENT_INPUT, comment)
        
        # Кнопка "Заказать"
        self.click(self.ORDER_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.SUCCESS_MODAL))
    
    def confirm(self):
        self.click(self.CONFIRM_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))