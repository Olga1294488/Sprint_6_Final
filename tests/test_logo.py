import pytest
import allure
from selenium.webdriver.common.by import By
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
        original_window = driver.current_window_handle
        
        yandex_link = driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").get_attribute("href")
        
        driver.execute_script(f"window.open('{yandex_link}');")
        
        home_page.wait.until(lambda d: len(d.window_handles) > 1)
        
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break
        
        home_page.wait.until(lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url)
        
        current_url = driver.current_url
        driver.close()
        driver.switch_to.window(original_window)
        
        assert "dzen.ru" in current_url