from pages.base_page import BasePageObject


class Layer(BasePageObject):
    """Класс-посредник, хранящий шаблоны локаторов элементов и общие методы для работы со страницами."""

    """Шаблоны локаторов элементов."""
    list_item_by_data_id = "//li[@data-id='{}']"
