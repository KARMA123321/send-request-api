import config
import requests

from src.responses.base_response import BaseResponse
from jsonschema.validators import validate
from src.enums.schemas.schemas_names import SchemasNames
from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_keys.company_list import CompanyList


class GetCompaniesResponse(BaseResponse):
    STATUS_QUERY = "status"
    LIMIT_QUERY = "limit"
    OFFSET_QUERY = "offset"

    def __init__(self, **kwargs):
        response = requests.get(config.FULL_URL + "/companies", **kwargs)
        super().__init__(response)

    def assert_schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.CompanyList}")
        validate(self.response_json, schemas[SchemasNames.CompanyList])
        return self

    def assert_companies_statuses(self, expected_status):
        print("Assert companies statuses")

        error = "Expected company status to be '{0}', but was '{1}'"
        for company in self.response_json[CompanyList.Data]:
            statuses_equality = company[Company.Status] == expected_status
            print(f"{company[Company.Name]} status equal to {expected_status} [{statuses_equality}]")
            assert statuses_equality, error.format(expected_status, company[Company.Status])
