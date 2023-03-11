from allure import step

from api_helper.base_requests import BaseRequest


class LayerRequests(BaseRequest):
    """Класс-посредник, хранящий общие методы для работы с API запросами."""

    @staticmethod
    @step("Получение статус кода API запроса.")
    def get_status_code(api_response) -> str:  # api_response is class:`Response <Response>` object
        """
        Возвращает статус код.

        :param api_response: Ответ на запрос.
        """
        return str(api_response.status_code)

    @staticmethod
    @step("Получение текста ответа на API запрос.")
    def get_text(api_response) -> str:  # api_response is class:`Response <Response>` object
        """
        Возвращает текст ответа на запрос.

        :param api_response: Ответ на запрос.
        """
        return api_response.text.replace(' ', '')
