import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Открытие страницы {url}')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Клик на сообщение с согласием на использование cookie')
    def click_to_cookie(self):
        self.find_element_with_wait(MainPageLocators.COOKIE_LOCATOR).click()

    @allure.step('Скролл страницы до последнего вопроса')
    def scroll_into_questions(self):
        element = self.find_element_with_wait(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Клик на стрелку с вопросом {question}')
    def click_to_question(self, question):
        locator_question = self.format_locator(MainPageLocators.QUESTION_LOCATOR, question)
        self.find_element_with_wait(locator_question).click()

    @allure.step('Получение ответа на вопрос {question}')
    def get_answer_text(self, question):
        locator_answers = self.format_locator(MainPageLocators.ANSWER_LOCATOR, question)
        return self.find_element_with_wait(locator_answers).text

    @allure.step('Клик на кнопку "Заказать"')
    def click_to_button_order(self, locator):
        self.click_to_element(locator)