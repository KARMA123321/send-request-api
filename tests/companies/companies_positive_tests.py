import allure
import pytest

from src.asserts import Assert
from src.enums.schemas.schemas_keys.company import Company
from src.responses.companies.get_companies_response import GetCompaniesResponse, STATUS_QUERY, LIMIT_QUERY, OFFSET_QUERY
from src.enums.company_statuses import CompanyStatuses
from src.responses.companies.get_company_by_id_response import GetCompanyByIdResponse


@allure.title("GET /api/companies schema and status code are valid")
def test_get_companies_schema_and_status_code(schemas):
    GetCompaniesResponse().validate.schema(schemas).validate.status_code_equals(200)


@allure.title("GET /api/companies with status '{company_status}'")
@pytest.mark.parametrize("company_status", [CompanyStatuses.ACTIVE, CompanyStatuses.BANKRUPT,
                                            CompanyStatuses.CLOSED])
def test_get_companies_filter_by_status(company_status):
    GetCompaniesResponse(params={STATUS_QUERY: company_status}).validate.companies_statuses_equal_to(company_status)


@allure.title("GET /api/companies with limit '{value}' and offset '{value}'")
@pytest.mark.parametrize("value", [0, 3])
def test_get_companies_filter_by_limit_and_offset(value):
    Assert.multiple(
        lambda: GetCompaniesResponse(params={LIMIT_QUERY: value}).validate.companies_amount_equal_to_limit(value),
        lambda: GetCompaniesResponse(params={OFFSET_QUERY: value}).validate.companies_start_from_offset(value)
    )


@allure.title("GET /api/companies/{company_id} schema and status code are valid")
def test_get_company_by_id_schema_and_status_code(random_company, schemas):
    GetCompanyByIdResponse(random_company[Company.Id]).validate.schema(schemas).validate.status_code_equals(200)
