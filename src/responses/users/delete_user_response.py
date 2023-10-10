import requests

import config
from src.responses.base_response import BaseResponse


class DeleteUserResponse(BaseResponse):
    def __init__(self, user_id, **request_attributes):
        self.response = requests.delete(config.FULL_URL + f"/users/{user_id}")
        super().__init__(self.response)
