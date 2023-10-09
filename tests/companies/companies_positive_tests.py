import pytest

from src.responses.companies.get_companies_response import GetCompaniesResponse, STATUS_QUERY, LIMIT_QUERY, OFFSET_QUERY
from src.enums.company_statuses import CompanyStatuses


def test_get_companies_schema_and_status_code(schemas):
    GetCompaniesResponse().assert_schema(schemas).assert_status_code(200)


@pytest.mark.parametrize("company_status", [CompanyStatuses.ACTIVE, CompanyStatuses.BANKRUPT,
                                            CompanyStatuses.CLOSED])
def test_get_companies_filter_by_status(company_status):
    GetCompaniesResponse(params={STATUS_QUERY: company_status}).assert_companies_statuses(company_status)


@pytest.mark.parametrize("value", [0, 3])
def test_get_companies_filter_by_limit_and_offset(value):
    GetCompaniesResponse(params={LIMIT_QUERY: value}).assert_equal_to_limit(value)
    GetCompaniesResponse(params={OFFSET_QUERY: value}).assert_starts_from_offset(value)
