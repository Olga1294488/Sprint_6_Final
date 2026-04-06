from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import Urls
import allure


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    # === Базовые методы работы с элементами ===
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def click_js(self, element):
        self._driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self._driver.execute_script("arguments[0].click();", element)
    
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        return self.find_element(locator).text
    
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)
    
    # === Методы для работы с URL и окнами ===
    def get_current_url(self):
        return self._driver.current_url
    
    def open_url(self, url):
        self._driver.get(url)
    
    def scroll_to_bottom(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def open_link_in_new_tab(self, url):
        self._driver.execute_script(f"window.open('{url}');")
    
    def wait_for_new_window(self, expected_count=2):
        self.wait.until(lambda d: len(d.window_handles) == expected_count)
    
    def switch_to_last_window(self):
        handles = self._driver.window_handles
        self._driver.switch_to.window(handles[-1])
    
    def switch_to_window_by_handle(self, window_handle):
        self._driver.switch_to.window(window_handle)
    
    def close_current_window(self):
        self._driver.close()
    
    def get_current_window_handle(self):
        return self._driver.current_window_handle
    
    # === Методы для ожиданий ===
    def wait_for_url_contains(self, text):
        self.wait.until(lambda d: text in d.current_url)
    
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self._driver.get(url)
    def get_current_window_handle(self):
        return self._driver.current_window_handle