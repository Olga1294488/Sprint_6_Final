import pytest
import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.order_confirmation_page import OrderConfirmationPage
from data.order_data import OrderData


@allure.feature("Оформление заказа")
class TestOrder:
    
    @allure.title("Позитивный сценарий заказа самоката (кнопка вверху)")
    def test_create_order_top(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            OrderData.ORDER_TOP["name"],
            OrderData.ORDER_TOP["surname"],
            OrderData.ORDER_TOP["address"],
            OrderData.ORDER_TOP["metro"],
            OrderData.ORDER_TOP["phone"]
        )
        order_page.fill_second_form_black_with_comment(
            OrderData.ORDER_TOP["date"],
            OrderData.ORDER_TOP["period"],
            OrderData.ORDER_TOP["comment"]
        )
        order_page.confirm()
        
        confirmation_page = OrderConfirmationPage(driver)
        assert confirmation_page.is_successful()
    
    @allure.title("Позитивный сценарий заказа самоката (кнопка внизу)")
    def test_create_order_bottom(self, driver):
        home_page = HomePage(driver)
        home_page.scroll_to_bottom()
        home_page.click_order_bottom()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            OrderData.ORDER_BOTTOM["name"],
            OrderData.ORDER_BOTTOM["surname"],
            OrderData.ORDER_BOTTOM["address"],
            OrderData.ORDER_BOTTOM["metro"],
            OrderData.ORDER_BOTTOM["phone"]
        )
        order_page.fill_second_form_grey_with_comment(
            OrderData.ORDER_BOTTOM["date"],
            OrderData.ORDER_BOTTOM["period"],
            OrderData.ORDER_BOTTOM["comment"]
        )
        order_page.confirm()
        
        confirmation_page = OrderConfirmationPage(driver)
        assert confirmation_page.is_successful()