from dataclasses import dataclass


@dataclass
class MainPageData:
    """Класс, хранящий data id элементов на главной странице."""

    list_users: str = "users"
    single_user: str = "users-single"
    single_user_not_found: str = "users-single-not-found"
    list_resource: str = "unknown"
    single_resource: str = "unknown-single"
    single_resource_not_found: str = "unknown-single-not-found"
    post: str = "post"
    put: str = "put"
    patch: str = "patch"
    delete: str = "delete"
    register_successful: str = "register-successful"
    register_unsuccessful: str = "register-unsuccessful"
    login_successful: str = "login-successful"
    login_unsuccessful: str = "login-unsuccessful"
    delayed_response: str = "delay"
