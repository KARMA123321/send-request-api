import allure
from pytest_check import check

from src.responses.users.get_user_by_id_response import GetUserByIdResponse


@allure.title("POST /api/users schema and status code are valid")
def test_create_user_schema_and_status_code(new_user, schemas):
    new_user.validate.schema(schemas).validate.status_code_equals(201)


@allure.title("POST /api/users create user with specified params")
def test_specified_user_created(new_user, schemas):
    GetUserByIdResponse(new_user.user_id).validate.user_equals(**new_user.response_json)


@allure.title("POST /api/users/{user_id} schema and status code are valid")
def test_get_user_by_id_schema_and_status_code(new_user, schemas):
    GetUserByIdResponse(new_user.user_id).validate.schema(schemas).validate.status_code_equals(200)



