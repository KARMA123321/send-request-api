import requests
import config

from src.responses.companies.get_companies_response import GetCompaniesResponse
from src.responses.base_response import BaseResponse


def test_get_companies(schemas):
    response = GetCompaniesResponse()
    response.validate_against_schema(schemas["CompanyList"])
