import requests

import config
from src.responses.base_response import BaseResponse


class DeleteUserResponse(BaseResponse):
    def __init__(self, user_id, **request_attributes):
        super().__init__(requests.delete(config.FULL_URL + f"/users/{user_id}", **request_attributes))
