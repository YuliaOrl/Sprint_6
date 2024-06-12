import pytest
import allure

from data import *
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.header_page import HeaderPage
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators


class TestYandexScooter:

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('Проверяется нажатие на стрелку с вопросом и открытие текста с ответом.')
    @pytest.mark.parametrize('question, result', TEST_DATA)
    def test_questions_and_answers(self, driver, question, result):
        main_page = MainPage(driver)
        main_page.get_url(MAIN_URL)
        main_page.click_to_cookie()
        main_page.scroll_into_questions()
        main_page.click_to_question(question)
        assert main_page.get_answer_text(question) == result

    @allure.title('Позитивная проверка создания заказа')
    @allure.description('Проверяется создание заказа с корректными данными')
    @pytest.mark.parametrize('order_button', [MainPageLocators.FIRST_ORDER_BUTTON, MainPageLocators.MIDLE_ORDER_BUTTON])
    def test_order(self, driver, order_button):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.get_url(MAIN_URL)
        main_page.click_to_cookie()
        main_page.click_to_button_order(order_button)
        order_page.set_order()
        assert EXPECTED_MESSAGE in order_page.get_message_order()

    @allure.title('Проверка переходов на страницы по нажатию на логотипы в хедере')
    @allure.description('Проверяется переход по банеру на главную страницу "Самокат" и "Дзен"')
    @pytest.mark.parametrize('logo, num, title_locator, expected_title',
                             [['Scooter', 0, HeaderPageLocators.TITLE_SCOOTER_LOCATOR, 'Самокат'],
                              ['Yandex', 1, HeaderPageLocators.TITLE_DZEN_LOCATOR, 'Новости']])
    def test_switch_from_banner_scooter_and_yandex(self, driver, logo, num, title_locator, expected_title):
        header_page = HeaderPage(driver)
        header_page.get_url(ORDER_URL)
        header_page.click_to_logo(logo)
        header_page.switch_to_page(num)
        assert expected_title in header_page.get_title_page(title_locator)
