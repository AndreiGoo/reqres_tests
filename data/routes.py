from dataclasses import dataclass


@dataclass
class Routes:
    """Класс, хранящий url страниц."""

    main_page: str = "https://reqres.in/"
