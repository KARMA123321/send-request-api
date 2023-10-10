import requests
from jsonschema.validators import validate

import config
from src.enums.schemas.schemas_names import SchemasNames
from src.responses.base_response import BaseResponse


class CreateUserResponse(BaseResponse):
    def __init__(self, **request_attributes):
        self.response = requests.post(config.FULL_URL + "/users", **request_attributes)
        super().__init__(self.response)
        self.first_name = self.response_json["first_name"]
        self.last_name = self.response_json["last_name"]
        self.company_id = self.response_json["company_id"]
        self.user_id = self.response_json["user_id"]

    def assert_schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.ResponseUser}")
        validate(self.response_json, schemas[SchemasNames.ResponseUser])
        return self

