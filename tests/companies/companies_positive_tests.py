import requests
import config

from src.responses.companies.get_companies_response import GetCompaniesResponse
from src.responses.base_response import BaseResponse
from tests.conftest import schemas


def test_get_companies(schemas):
    response = GetCompaniesResponse(params={"limit": 2})
    response.validate_against_schema(schemas["CompanyList"])
