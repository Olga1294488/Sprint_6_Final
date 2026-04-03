import pytest
from pages.home_page import HomePage


class TestLogo:
    def test_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_order_top()
        home_page.click_scooter_logo()
        assert "qa-scooter" in home_page.get_current_url()
    
    @pytest.mark.skip(reason="Требуется настройка переключения окон")
    def test_yandex_logo(self, driver):
        pass