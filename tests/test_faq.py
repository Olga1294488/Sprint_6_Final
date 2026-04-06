import pytest
from pages.home_page import HomePage
from data.faq_data import FAQData


class TestFAQ:
    @pytest.mark.parametrize("index,expected", FAQData.QUESTIONS_ANSWERS)
    def test_faq_answer(self, driver, index, expected):
        home_page = HomePage(driver)
        home_page.click_question(index)
        actual = home_page.get_answer_text()
        assert actual == expected