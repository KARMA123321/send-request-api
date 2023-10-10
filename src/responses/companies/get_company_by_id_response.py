import requests
from jsonschema.validators import validate

import config
from src.enums.schemas.schemas_names import SchemasNames
from src.responses.base_response import BaseResponse


class GetCompanyByIdResponse(BaseResponse):
    def __init__(self, company_id, **request_attributes):
        super().__init__(requests.get(config.FULL_URL + f"/companies/{company_id}", **request_attributes))

    def assert_schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.Company}")
        validate(self.response_json, schemas[SchemasNames.Company])
        return self
