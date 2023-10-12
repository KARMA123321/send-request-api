import allure
from jsonschema.validators import validate

from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_names import SchemasNames
from src.interfaces.response_validation_interface import ResponseValidationInterface
from src.validation_managers.base_validation_manager import BaseValidationManager


class GetCompaniesValidationManager(BaseValidationManager, ResponseValidationInterface):
    def __init__(self, response):
        super().__init__(response)

    def schema(self, schemas):
        with allure.step(f"Response matches schema {SchemasNames.CompanyList}"):
            validate(self.response.response_json, schemas[SchemasNames.CompanyList])
        return self.response

    def companies_statuses_equal_to(self, expected_status):
        with allure.step(f"Companies statuses are equal to '{expected_status}'"):
            errors = ""
            for company in self.response.companies:
                if company[Company.Status] != expected_status:
                    errors += f"\n{company[Company.Name]}, status: {company[Company.Status]}"

            assert len(errors) == 0, errors + self.response.__str__()
        return self.response

    def companies_amount_equal_to_limit(self, limit):
        with allure.step(f"Companies amount is equal to the limit = {limit}"):
            assert len(self.response.companies) == limit, \
                f"Expected number of companies is {limit} but there was {len(self.response.companies)}" \
                + self.response.__str__()
        return self.response

    def companies_start_from_offset(self, offset):
        with allure.step(f"Companies start with offset = {offset}"):
            expected_id = offset + 1
            first_id = self.response.companies[0][Company.Id]

            assert first_id == expected_id, \
                f"Expected first company's id to be {expected_id} but was {first_id}" + self.response.__str__()
        return self.response
