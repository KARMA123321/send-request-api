import allure
from jsonschema.validators import validate
from pytest_check import check

from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.enums.schemas.schemas_names import SchemasNames
from src.interfaces.response_validation_interface import ResponseValidationInterface
from src.validation_managers.base_validation_manager import BaseValidationManager


class BaseUserValidationManager(BaseValidationManager, ResponseValidationInterface):
    def __init__(self, response):
        super().__init__(response)
        self.first_name = response.response_json[ResponseUser.FirstName]
        self.last_name = response.response_json[ResponseUser.LastName]
        self.company_id = response.response_json[ResponseUser.CompanyId]
        self.user_id = response.response_json[ResponseUser.UserId]

    def schema(self, schemas):
        with allure.step(f"Response matches schema {SchemasNames.ResponseUser}"):
            validate(self.response.response_json, schemas[SchemasNames.ResponseUser])
        return self.response

    def user_equals_params(self, **user_params):
        with allure.step(f"Response user matches specified parameters: "
                         f"id: {user_params[ResponseUser.UserId]}, "
                         f"name: {user_params[ResponseUser.FirstName]}, "
                         f"last name: {user_params[ResponseUser.LastName]}, "
                         f"company: {user_params[ResponseUser.CompanyId]}"):
            assert user_params == self.response.response_json, \
                f"\n{user_params} is not equal to {self.response.response_json}" + str(self.response)

    def user_equals(self, user_id, first_name, last_name, company_id):
        with allure.step(f"Response user matches specified parameters: "
                         f"id: {user_id}, "
                         f"name: {first_name}, "
                         f"last name: {last_name}, "
                         f"company: {company_id}"):
            user = dict(user_id=user_id, first_name=first_name, last_name=last_name, company_id=company_id)
            assert user == self.response.response_json, \
                f"\n{user} is not equal to {self.response.response_json}" + str(self.response)
