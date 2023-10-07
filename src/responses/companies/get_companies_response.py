from src.responses.base_response import BaseResponse

import config
import requests


class GetCompaniesResponse(BaseResponse):
    def __init__(self):
        response = requests.get(config.FULL_URL + "/companies")
        super().__init__(response)
