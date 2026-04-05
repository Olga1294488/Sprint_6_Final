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
        original_window = home_page.switch_to_new_window()
        
        home_page.wait.until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
        
        current_url = home_page.get_current_url()
        home_page.close_current_window_and_switch_back(original_window)
        
        assert "dzen.ru" in current_url