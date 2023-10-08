import config
import requests

from src.responses.base_response import BaseResponse
from jsonschema.validators import validate
from src.enums.schemas.schemas_names import SchemasNames
from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_keys.company_list import CompanyList


STATUS_QUERY = "status"
LIMIT_QUERY = "limit"
OFFSET_QUERY = "offset"


class GetCompaniesResponse(BaseResponse):
    def __init__(self, **kwargs):
        response = requests.get(config.FULL_URL + "/companies", **kwargs)
        super().__init__(response)
        self.companies = self.response_json[CompanyList.Data]

    def assert_schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.CompanyList}")
        validate(self.response_json, schemas[SchemasNames.CompanyList])
        return self

    def assert_companies_statuses(self, expected_status):
        print("Assert companies statuses")

        errors = ""
        for company in self.companies:
            status_equality = company[Company.Status] == expected_status
            print(f"{company[Company.Name]} status equal to {expected_status} [{status_equality}]")
            if not status_equality:
                errors += f"\n{company[Company.Name]}, status: {company[Company.Status]}"

        assert len(errors) == 0, errors + self.__str__()
