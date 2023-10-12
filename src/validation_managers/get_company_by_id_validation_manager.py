import allure
from jsonschema.validators import validate

from src.enums.schemas.schemas_names import SchemasNames
from src.interfaces.response_validation_interface import ResponseValidationInterface
from src.validation_managers.base_validation_manager import BaseValidationManager


class GetCompanyByIdValidationManager(BaseValidationManager, ResponseValidationInterface):
    def __init__(self, response):
        super().__init__(response)

    def schema(self, schemas):
        with allure.step(f"Response matches schema {SchemasNames.Company}"):
            validate(self.response.response_json, schemas[SchemasNames.Company])
        return self.response
