from dataclasses import dataclass


@dataclass
class TestData:
    """Класс, хранящий тестовые данные."""

    users_page: str = "2"
    user_id: str = "2"
    non_existent_user_id: str = "23"
    resource_id: str = "2"
    non_existent_resource_id: str = "23"
    new_user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    user_updated_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    successful_registration_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    unsuccessful_registration_data = {
        "email": "sydney@fife"
    }
    successful_login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    unsuccessful_login_data = {
        "email": "peter@klaven"
    }
    users_delay: str = "3"
