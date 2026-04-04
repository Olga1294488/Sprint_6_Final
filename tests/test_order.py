import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_confirmation_page import OrderConfirmationPage


@allure.feature("Оформление заказа")
class TestOrder:
    
    @pytest.mark.parametrize("button_type", ["top", "bottom"])
    @allure.title("Позитивный сценарий заказа самоката (кнопка: {button_type})")
    def test_create_order(self, driver, button_type):
        home_page = HomePage(driver)
        
        if button_type == "top":
            home_page.click_order_top()
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            home_page.click_order_bottom()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form("Анна", "Петрова", "ул. Ленина, 10", "Сокольники", "89991234567")
        order_page.fill_second_form("01.12.2024", "сутки", "black", "Позвоните за 15 минут")
        order_page.confirm()
        
        confirmation_page = OrderConfirmationPage(driver)
        assert confirmation_page.is_successful()