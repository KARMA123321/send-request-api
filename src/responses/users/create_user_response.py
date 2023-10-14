import requests

import config
from src.responses.users.base_user_response import BaseUserResponse
from src.validation_managers.users.create_user_validation_manager import CreateUserValidationManager


class CreateUserResponse(BaseUserResponse):
    def __init__(self, **request_attributes):
        super().__init__(requests.post(config.FULL_URL + "/users", **request_attributes))

        self.validate: CreateUserValidationManager = CreateUserValidationManager(self)
