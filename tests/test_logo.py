import pytest
import allure
from pages.home_page import HomePage


@allure.feature("Навигация по логотипам")
class TestLogo:
    
    @allure.title("Переход на главную страницу по логотипу Самоката")
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.click_scooter_logo()
        assert "qa-scooter" in home_page.get_current_url()
    
    @allure.title("Переход на Дзен по логотипу Яндекса")
    def test_yandex_logo(self, driver):
        home_page = HomePage(driver)
        
        yandex_link = home_page.get_yandex_logo_link()
        home_page.open_link_in_new_tab(yandex_link)
        home_page.wait_for_new_window()
        home_page.switch_to_last_window()
        home_page.wait_for_url_contains_dzen()
        
        current_url = home_page.get_current_url()
        home_page.close_current_window()
        home_page.switch_to_original_window(home_page.get_current_window_handle())
        
        assert "dzen.ru" in current_url