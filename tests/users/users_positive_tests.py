def test_create_user_schema_and_status_code(new_user, schemas):
    new_user.assert_schema(schemas).assert_status_code(201)
