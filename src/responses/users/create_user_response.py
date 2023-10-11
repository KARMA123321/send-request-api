import requests

import config
from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.responses.base_response import BaseResponse
from src.validation_managers.create_user_validation_manager import CreateUserValidationManager


class CreateUserResponse(BaseResponse):
    def __init__(self, **request_attributes):
        super().__init__(requests.post(config.FULL_URL + "/users", **request_attributes))
        self.first_name = self.response_json[ResponseUser.FirstName]
        self.last_name = self.response_json[ResponseUser.LastName]
        self.company_id = self.response_json[ResponseUser.CompanyId]
        self.user_id = self.response_json[ResponseUser.UserId]

        self.validate: CreateUserValidationManager = CreateUserValidationManager(self)
