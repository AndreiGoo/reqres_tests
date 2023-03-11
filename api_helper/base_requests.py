import requests

from allure import step


class BaseRequest:
    """Класс, предоставляющий базовые методы для работы с API."""

    @staticmethod
    @step("GET-запрос.")
    def get(url: str, json: dict = None, headers: dict = None):  # -> class:`Response <Response>` object
        """
        Выполняет get-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса.
        :param json: Тело запроса.
        :param headers: Заголовки.
        """
        response = requests.get(url=url,
                                json=json,
                                headers=headers)
        return response

    @staticmethod
    @step("POST-запрос.")
    def post(url: str, json: dict = None, headers: dict = None):  # -> class:`Response <Response>` object
        """
        Выполняет post-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса.
        :param json: Тело запроса.
        :param headers: Заголовки.
        """
        response = requests.post(url=url,
                                 json=json,
                                 headers=headers)
        return response

    @staticmethod
    @step("PUT-запрос.")
    def put(url: str, json: dict = None, headers: dict = None):  # -> class:`Response <Response>` object
        """
        Выполняет put-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса.
        :param json: Тело запроса.
        :param headers: Заголовки.
        """
        response = requests.put(url=url,
                                json=json,
                                headers=headers)
        return response

    @staticmethod
    @step("PATCH-запрос.")
    def patch(url: str, json: dict = None, headers: dict = None):  # -> class:`Response <Response>` object
        """
        Выполняет put-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса.
        :param json: Тело запроса.
        :param headers: Заголовки.
        """
        response = requests.put(url=url,
                                json=json,
                                headers=headers)
        return response

    @staticmethod
    @step("DELETE-запрос.")
    def delete(url: str, json: dict = None, headers: dict = None):  # -> class:`Response <Response>` object
        """
        Выполняет delete-запрос, затем возвращает ответ на него.

        :param url: URL-адрес запроса.
        :param json: Тело запроса.
        :param headers: Заголовки.
        """
        response = requests.delete(url=url,
                                   json=json,
                                   headers=headers)
        return response
