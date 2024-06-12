from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_LOCATOR = By.CSS_SELECTOR, ".App_CookieButton__3cvqF"  # Локатор cookie
    QUESTION_LOCATOR = ".//div[@class='accordion__button' and contains(text(), '{}')]"  # Общий локатор вопроса
    ANSWER_LOCATOR = QUESTION_LOCATOR + "/parent::div/following-sibling::div"  # Общий локатор ответа
    LAST_QUESTION_LOCATOR = By.XPATH, ".//div[@class='accordion']/div[last()]"  # Локатор последнего вопроса
    FIRST_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g']"  # Локатор первой кнопки "Заказать"
    MIDLE_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # Локатор второй
    # кнопки "Заказать"
