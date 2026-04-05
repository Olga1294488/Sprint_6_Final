from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage, HomePageLocators):
    
    def click_order_top(self):
        button = self.find_element(self.ORDER_BUTTON_TOP)
        self.click_js(button)
    
    def click_order_bottom(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_BOTTOM))
        self.click_js(button)
    
    def click_question(self, index):
        questions = self.find_elements(self.ACCORDION_BUTTON)
        self.click_js(questions[index])
        self.wait.until(EC.visibility_of_element_located(self.VISIBLE_ACCORDION_PANEL))
    
    def get_answer_text(self):
        return self.get_text(self.VISIBLE_ACCORDION_PANEL)
    
    def click_scooter_logo(self):
        self.click_js(self.find_element(self.SCOOTER_LOGO))
    
    def click_yandex_logo(self):
        logo = self.find_element(self.YANDEX_LOGO)
        self.click_js(logo)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def get_yandex_logo_link(self):
        return self.find_element(self.YANDEX_LOGO).get_attribute("href")
    
    def open_link_in_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}');")
    
    def switch_to_last_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
    
    def switch_to_original_window(self, original_window):
        self.driver.switch_to.window(original_window)
    
    def close_current_window(self):
        self.driver.close()