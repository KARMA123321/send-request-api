from jsonschema.validators import validate

from src.enums.schemas.schemas_names import SchemasNames
from src.interfaces.response_validation_interface import ResponseValidationInterface
from src.validation_managers.base_validation_manager import BaseValidationManager


class CreateUserValidationManager(BaseValidationManager, ResponseValidationInterface):
    def __init__(self, response):
        super().__init__(response)

    def schema(self, schemas):
        print(f"Assert schema matches {SchemasNames.ResponseUser}")
        validate(self.response.response_json, schemas[SchemasNames.ResponseUser])
        return self.response
