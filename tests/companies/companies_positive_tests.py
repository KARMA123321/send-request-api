import pytest

from src.responses.companies.get_companies_response import GetCompaniesResponse
from src.enums.company_statuses import CompanyStatuses
from conftest import schemas


def test_get_companies_schema_and_status_code(schemas):
    GetCompaniesResponse().assert_schema(schemas).assert_status_code(200)


@pytest.mark.parametrize("status", [CompanyStatuses.ACTIVE, CompanyStatuses.BANKRUPT,
                                    CompanyStatuses.CLOSED])
def test_get_companies_filter_by_status(status):
    GetCompaniesResponse(params={GetCompaniesResponse.STATUS_QUERY: status}).assert_companies_statuses(status)
