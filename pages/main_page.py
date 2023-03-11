from selenium.webdriver.common.by import By

from allure import step

from pages.layer import Layer


class MainPage(Layer):
    """Класс, предоставляющий методы для работы с главной страницей."""

    @step("Выбор запроса с главной страницы.")
    def choose_request(self, request_name: str) -> None:
        """
        Выбирает запрос на главной странице.

        :param request_name: Название запроса.
        """
        self.click(By.XPATH, self.list_item_by_data_id.format(request_name))

    @step("Получение статус кода с фронта.")
    def get_response_code(self, api_code: str) -> str:
        """
        Возвращает статус код.

        :param api_code: Ожидаемый статус код.
        """
        return self.wait_element_with_text(By.XPATH, '//span[@data-key="response-code"]', api_code).text

    @step("Получение текста ответа на запрос с фронта.")
    def get_response_text(self) -> str:
        """
        Возвращает текст ответа на запрос.
        """
        return \
            self.wait_visibility(By.XPATH, '//pre[@data-key="output-response"]').text.replace("\n", "").replace(" ", "")
