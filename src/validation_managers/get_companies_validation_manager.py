from jsonschema.validators import validate

from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_names import SchemasNames
from src.interfaces.response_validation_interface import ResponseValidationInterface
from src.validation_managers.base_validation_manager import BaseValidationManager


class GetCompaniesValidationManager(BaseValidationManager, ResponseValidationInterface):
    def __init__(self, response):
        super().__init__(response)

    def schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.CompanyList}")
        validate(self.response.response_json, schemas[SchemasNames.CompanyList])
        return self.response

    def companies_statuses_equal_to(self, expected_status):
        print("Assert companies statuses")

        errors = ""
        for company in self.response.companies:
            status_equality = company[Company.Status] == expected_status
            print(f"{company[Company.Name]} status equal to {expected_status} [{status_equality}]")
            if not status_equality:
                errors += f"\n{company[Company.Name]}, status: {company[Company.Status]}"

        assert len(errors) == 0, errors + self.response.__str__()
        return self.response

    def companies_amount_equal_to_limit(self, limit):
        print(f"Assert that the number of companies is equal to {limit}")
        assert len(self.response.companies) == limit, \
            f"Expected number of companies is {limit} but there was {len(self.response.companies)}" \
            + self.response.__str__()
        return self.response

    def companies_start_from_offset(self, offset):
        expected_id = offset + 1
        first_id = self.response.companies[0][Company.Id]

        print(f"Assert that companies list starts with company with id '{expected_id}'")
        assert first_id == expected_id, \
            f"Expected first company's id to be {expected_id} but was {first_id}" + self.response.__str__()
        return self.response
