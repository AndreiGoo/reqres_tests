import pytest

from allure import title, severity

from api_helper.base_requests import BaseRequest
from api_helper.layer_requests import LayerRequests
from data.main_page_data import MainPageData
from data.requests_url import RequestsUrl
from data.test_data import TestData


@title("Сравнение ответов на запросы с фронта и на API запросы.")
@severity("Normal")
@pytest.mark.parametrize("request_name, api_response",
                         [
                             pytest.param(MainPageData.list_users,
                                          BaseRequest.get(
                                              RequestsUrl.base_api + RequestsUrl.list_users.format(
                                                  TestData.users_page))),

                             pytest.param(MainPageData.single_user,
                                          BaseRequest.get(
                                              RequestsUrl.base_api + RequestsUrl.single_user.format(TestData.user_id))),

                             pytest.param(MainPageData.single_user_not_found,
                                          BaseRequest.get(
                                              RequestsUrl.base_api + RequestsUrl.single_user.format(
                                                  TestData.non_existent_user_id))),

                             pytest.param(MainPageData.list_resource,
                                          BaseRequest.get(RequestsUrl.base_api + RequestsUrl.list_resource)),

                             pytest.param(MainPageData.single_resource,
                                          BaseRequest.get(
                                              RequestsUrl.base_api + RequestsUrl.single_resource.format(
                                                  TestData.resource_id))),

                             pytest.param(MainPageData.single_resource_not_found,
                                          BaseRequest.get(RequestsUrl.base_api + RequestsUrl.single_resource.format(
                                              TestData.non_existent_resource_id))),

                             pytest.param(MainPageData.post,
                                          BaseRequest.post(RequestsUrl.base_api + RequestsUrl.post,
                                                           TestData.new_user_data)),

                             pytest.param(MainPageData.put,
                                          BaseRequest.put(
                                              RequestsUrl.base_api + RequestsUrl.put.format(TestData.user_id),
                                              TestData.user_updated_data)),

                             pytest.param(MainPageData.patch,
                                          BaseRequest.patch(
                                              RequestsUrl.base_api + RequestsUrl.put.format(TestData.user_id),
                                              TestData.user_updated_data)),

                             pytest.param(MainPageData.delete,
                                          BaseRequest.delete(
                                              RequestsUrl.base_api + RequestsUrl.delete.format(TestData.user_id))),

                             pytest.param(MainPageData.register_successful,
                                          BaseRequest.post(RequestsUrl.base_api + RequestsUrl.register,
                                                           TestData.successful_registration_data)),

                             pytest.param(MainPageData.register_unsuccessful,
                                          BaseRequest.post(RequestsUrl.base_api + RequestsUrl.register,
                                                           TestData.unsuccessful_registration_data)),

                             pytest.param(MainPageData.login_successful,
                                          BaseRequest.post(RequestsUrl.base_api + RequestsUrl.login,
                                                           TestData.successful_login_data)),

                             pytest.param(MainPageData.login_unsuccessful,
                                          BaseRequest.post(RequestsUrl.base_api + RequestsUrl.login,
                                                           TestData.unsuccessful_login_data)),

                             pytest.param(MainPageData.delayed_response,
                                          BaseRequest.get(
                                              RequestsUrl.base_api + RequestsUrl.delayed_response.format(
                                                  TestData.users_delay))),
                         ])
def test(main_page, request_name, api_response):
    main_page.choose_request(request_name)
    api_code = LayerRequests.get_status_code(api_response)
    api_text = LayerRequests.get_text(api_response)
    ui_code = main_page.get_response_code(api_code)
    ui_text = main_page.get_response_text()
    assert api_code == ui_code, "Коды статусов не совпадают."
    assert api_text == ui_text, "Тексты запросов не совпадают."
