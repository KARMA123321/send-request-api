import requests
from jsonschema.validators import validate

import config
from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.enums.schemas.schemas_names import SchemasNames
from src.responses.base_response import BaseResponse


class CreateUserResponse(BaseResponse):
    def __init__(self, **request_attributes):
        super().__init__(requests.post(config.FULL_URL + "/users", **request_attributes))
        self.first_name = self.response_json[ResponseUser.FirstName]
        self.last_name = self.response_json[ResponseUser.LastName]
        self.company_id = self.response_json[ResponseUser.CompanyId]
        self.user_id = self.response_json[ResponseUser.UserId]

    def assert_schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.ResponseUser}")
        validate(self.response_json, schemas[SchemasNames.ResponseUser])
        return self

