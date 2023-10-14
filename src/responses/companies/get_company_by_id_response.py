import requests

import config
from src.responses.base_response import BaseResponse
from src.validation_managers.companies.get_company_by_id_validation_manager import GetCompanyByIdValidationManager


class GetCompanyByIdResponse(BaseResponse):
    def __init__(self, company_id, **request_attributes):
        super().__init__(requests.get(config.FULL_URL + f"/companies/{company_id}", **request_attributes))

        self.validate: GetCompanyByIdValidationManager = GetCompanyByIdValidationManager(self)
