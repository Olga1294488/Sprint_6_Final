from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderConfirmationPage(BasePage, OrderPageLocators):
    
    @allure.step("Проверить успешное создание заказа")
    def is_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL)).is_displayed()