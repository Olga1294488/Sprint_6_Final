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
            OrderData.FIRST_ORDER["name"],
            OrderData.FIRST_ORDER["surname"],
            OrderData.FIRST_ORDER["address"],
            OrderData.FIRST_ORDER["metro"],
            OrderData.FIRST_ORDER["phone"]
        )
        order_page.fill_second_form_black_with_comment(
            OrderData.FIRST_ORDER["date"],
            OrderData.FIRST_ORDER["period"],
            OrderData.FIRST_ORDER["comment"]
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
            OrderData.SECOND_ORDER["name"],
            OrderData.SECOND_ORDER["surname"],
            OrderData.SECOND_ORDER["address"],
            OrderData.SECOND_ORDER["metro"],
            OrderData.SECOND_ORDER["phone"]
        )
        order_page.fill_second_form_grey_with_comment(
            OrderData.SECOND_ORDER["date"],
            OrderData.SECOND_ORDER["period"],
            OrderData.SECOND_ORDER["comment"]
        )
        order_page.confirm()
        
        confirmation_page = OrderConfirmationPage(driver)
        assert confirmation_page.is_successful()