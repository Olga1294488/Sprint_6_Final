from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage, HomePageLocators):
    
    def click_order_top(self):
        button = self.wait_for_element_clickable(self.ORDER_BUTTON_TOP)
        self.click_js(button)
    
    def click_order_bottom(self):
        button = self.wait_for_element_clickable(self.ORDER_BUTTON_BOTTOM)
        self.click_js(button)
    
    def click_question(self, index):
        questions = self.find_elements(self.ACCORDION_BUTTON)
        self.click_js(questions[index])
        self.wait_for_element_visible(self.VISIBLE_ACCORDION_PANEL)
    
    def get_answer_text(self):
        return self.get_text(self.VISIBLE_ACCORDION_PANEL)
    
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
    
    def get_yandex_logo_link(self):
        return self.get_attribute(self.YANDEX_LOGO, "href")
    
    def get_current_url(self):
        return super().get_current_url()
    
    def scroll_to_bottom(self):
        super().scroll_to_bottom()
    
    def open_link_in_new_tab(self, url):
        super().open_link_in_new_tab(url)
    
    def wait_for_new_window(self):
        super().wait_for_new_window()
    
    def switch_to_last_window(self):
        super().switch_to_last_window()
    
    def close_current_window(self):
        super().close_current_window()
    
    def switch_to_original_window(self, original_window):
        super().switch_to_window_by_handle(original_window)
    
    def wait_for_url_contains_dzen(self):
        self.wait_for_url_contains("dzen.ru")