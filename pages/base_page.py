from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c


class BasePageObject:
    """Класс, предоставляющий методы для работы с драйвером браузера."""

    def __init__(self, driver):
        """
        Инициализация драйвера.
        """
        self.driver = driver

    def wait_visibility(self, by: By, locator: str, timeout: int = 10) -> WebElement:
        """
        Ожидает видимости элемента на экране, затем возвращает его.

        :param by: Метод поиска локатора.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(e_c.visibility_of_element_located((by, locator)))

    def wait_element_with_text(self, by: By, locator: str, text: str, timeout: int = 10) -> WebElement:
        """
        Ожидает появления конкретного текста в элементе, затем возвращает элемент.

        :param by: Метод поиска локатора.
        :param locator: Локатор элемента.
        :param text: Ожидаемый текст элемента.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(e_c.text_to_be_present_in_element((by, locator), text))
        return self.driver.find_element(by, locator)

    def click(self, by: By, locator: str, timeout: int = 10) -> None:
        """
        Ожидает возможности кликнуть по элементу, затем кликает на него.

        :param by: Метод поиска локатора.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(e_c.element_to_be_clickable((by, locator))).click()
