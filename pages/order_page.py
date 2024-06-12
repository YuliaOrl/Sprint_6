import allure
from helpers import *
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Клик на кнопку {name}')
    def click_to_button(self, name):
        button_locator = self.format_locator(OrderPageLocators.BASE_BUTTON_LOCATOR, name)
        self.click_to_element(button_locator)

    @allure.step('Клик на кнопку "Заказать"')
    def click_to_button_order(self):
        self.click_to_element(OrderPageLocators.MIDLE_ORDER_BUTTON)

    @allure.step('Заполнение поля ввода {input_name}')
    def set_data(self, input_name, text):
        input_locator = self.format_locator(OrderPageLocators.INPUT_LOCATOR, input_name)
        self.add_text_to_element(input_locator, text)

    @allure.step('Выбор станции метро {metro}')
    def set_data_metro(self, input_name, metro):
        input_locator = self.format_locator(OrderPageLocators.INPUT_LOCATOR, input_name)
        self.click_to_element(input_locator)
        metro_locator = self.format_locator(OrderPageLocators.METRO_LOCATOR, metro)
        self.click_to_element(metro_locator)

    @allure.step('Выбор даты доставки {date}')
    def set_rental_date(self, input_name, date):
        date_locator = self.format_locator(OrderPageLocators.INPUT_LOCATOR, input_name)
        self.add_text_to_element(date_locator, date + Keys.ENTER)

    @allure.step('Выбор срока аренды {period}')
    def set_rental_period(self, period):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_LOCATOR)
        period_locator = self.format_locator(OrderPageLocators.PERIOD_LOCATOR, period)
        self.click_to_element(period_locator)

    @allure.step('Выбор чек-бокса с цветом самоката {color}')
    def set_color(self, color):
        color_locator = self.format_locator(OrderPageLocators.COLOR_LOCATOR, color)
        self.click_to_element(color_locator)

    @allure.step('Создание заказа')
    def set_order(self):
        self.set_data('Имя', OrderData.name)
        self.set_data('Фамилия', OrderData.surname)
        self.set_data('Адрес', OrderData.address)
        self.set_data_metro('Станция метро', OrderData.metro)
        self.set_data('Телефон', OrderData.phone)
        self.click_to_button('Далее')
        self.set_rental_date('Когда привезти самокат', OrderData.day)
        self.set_rental_period(OrderData.period)
        self.set_color(OrderData.color)
        self.set_data('Комментарий для курьера', OrderData.comment)
        self.click_to_button_order()
        self.click_to_button('Да')

    @allure.step('Получение сообщения "Заказ оформлен"')
    def get_message_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_MESSAGE_LOCATOR)
