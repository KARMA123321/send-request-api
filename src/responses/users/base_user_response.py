from requests import Response

from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.responses.base_response import BaseResponse


class BaseUserResponse(BaseResponse):
    def __init__(self, response: Response):
        super().__init__(response)
        self.first_name = self.response_json[ResponseUser.FirstName]
        self.last_name = self.response_json[ResponseUser.LastName]
        self.company_id = self.response_json[ResponseUser.CompanyId]
        self.user_id = self.response_json[ResponseUser.UserId]
