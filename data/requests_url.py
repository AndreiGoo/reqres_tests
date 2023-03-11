from dataclasses import dataclass


@dataclass
class RequestsUrl:
    """Класс, хранящий url API запросов."""

    base_api: str = "https://reqres.in/api"
    list_users: str = "/users?page={}"
    single_user: str = "/users/{}"
    list_resource: str = "/unknown"
    single_resource: str = "/unknown/{}"
    post: str = "/users"
    put: str = "/users/{}"
    patch: str = "/users/{}"
    delete: str = "/users/{}"
    register: str = "/register"
    login: str = "/login"
    delayed_response: str = "/users?delay={}"
