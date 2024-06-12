from selenium.webdriver.common.by import By


class HeaderPageLocators:
    BASE_LOGO_LOCATOR = ".//img[@alt='{}']"  # Общий локатор логотипа
    TITLE_SCOOTER_LOCATOR = By.CSS_SELECTOR, '.Home_Header__iJKdX'  # Локатор заголовка главной страницы Самокат
    TITLE_DZEN_LOCATOR = By.CSS_SELECTOR, '.floor-title__title-2v'  # Локатор заголовка Новости на главной странице ДЗЕН