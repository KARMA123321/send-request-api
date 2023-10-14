import config
import requests

from src.responses.base_response import BaseResponse
from src.enums.schemas.schemas_keys.company_list import CompanyList
from src.validation_managers.companies.get_companies_validation_manager import GetCompaniesValidationManager

STATUS_QUERY = "status"
LIMIT_QUERY = "limit"
OFFSET_QUERY = "offset"


class GetCompaniesResponse(BaseResponse):
    def __init__(self, **request_attributes):
        super().__init__(requests.get(config.FULL_URL + "/companies", **request_attributes))
        self.companies = self.response_json[CompanyList.Data]

        self.validate: GetCompaniesValidationManager = GetCompaniesValidationManager(self)
