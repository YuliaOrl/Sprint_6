from selenium.webdriver.common.by import By


class OrderPageLocators:

    INPUT_LOCATOR = ".//input[contains(@placeholder, '{}')]"  # Общий локатор поля ввода
    METRO_LOCATOR = ".//div[@class='Order_Text__2broi' and contains(text(), '{}')]"  # Общий локатор станции метро
    MIDLE_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"  # Локатор второй
    # кнопки "Заказать"

    BASE_BUTTON_LOCATOR = ".//button[contains(text(), '{}')]"  # Общий локатор кнопки

    RENTAL_PERIOD_LOCATOR = By.CSS_SELECTOR, ".Dropdown-placeholder"  # Локатор поля выбора срока аренды
    PERIOD_LOCATOR = ".//div[contains(text(), '{}')]"  # Общий локатор срока аренды

    COLOR_LOCATOR = ".//*[contains(text(), '{}')]"  # Общий локатор цвета
    DATE_LOCATOR = ".//*[contains(text(), '{}')]"  # Общий локатор даты

    ORDER_MESSAGE_LOCATOR = By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"  # Локатор сообщения успешного заказа
