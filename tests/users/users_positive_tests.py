import allure


@allure.title("POST /api/users schema and status code are valid")
def test_create_user_schema_and_status_code(new_user, schemas):
    new_user.validate.schema(schemas).validate.status_code_equals(201)
