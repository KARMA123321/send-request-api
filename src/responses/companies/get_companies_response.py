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
        return self

    def assert_equal_to_limit(self, limit):
        print(f"Assert that the number of companies is equal to {limit}")
        assert len(self.companies) == limit, \
            f"Expected number of companies is {limit} but there was {len(self.companies)}" + self.__str__()
        return self

    def assert_starts_from_offset(self, offset):
        expected_id = offset + 1
        first_id = self.companies[0][Company.Id]

        print(f"Assert that companies list starts with company with id '{expected_id}'")
        assert first_id == expected_id, \
            f"Expected first company's id to be {expected_id} but was {first_id}" + self.__str__()
        return self
