from src.responses.base_response import BaseResponse

import config
import requests


class GetCompaniesResponse(BaseResponse):
    def __init__(self, **kwargs):
        response = requests.get(config.FULL_URL + "/companies", **kwargs)
        super().__init__(response)
