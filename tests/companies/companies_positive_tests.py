import pytest

from src.responses.companies.get_companies_response import GetCompaniesResponse, STATUS_QUERY
from src.enums.company_statuses import CompanyStatuses
from conftest import schemas


def test_get_companies_schema_and_status_code(schemas):
    GetCompaniesResponse().assert_schema(schemas).assert_status_code(200)


@pytest.mark.parametrize("company_status", [CompanyStatuses.ACTIVE, CompanyStatuses.BANKRUPT,
                                            CompanyStatuses.CLOSED])
def test_get_companies_filter_by_status(company_status):
    GetCompaniesResponse(params={STATUS_QUERY: company_status})\
        .assert_companies_statuses(company_status)
