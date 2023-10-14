import requests

import config
from src.responses.users.base_user_response import BaseUserResponse
from src.validation_managers.users.get_user_by_id_validation_manager import GetUserByIdValidationManager


class GetUserByIdResponse(BaseUserResponse):
    def __init__(self, user_id, **request_attributes):
        super().__init__(requests.get(config.FULL_URL + f"/users/{user_id}", **request_attributes))

        self.validate: GetUserByIdValidationManager = GetUserByIdValidationManager(self)
