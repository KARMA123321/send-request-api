import json
import random
import string

import pytest

from config import COMPANIES_AMOUNT
from src.enums.company_statuses import CompanyStatuses
from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.responses.companies.get_companies_response import GetCompaniesResponse, LIMIT_QUERY, STATUS_QUERY
from src.responses.users.create_user_response import CreateUserResponse
from src.responses.users.delete_user_response import DeleteUserResponse


@pytest.fixture
def random_company():
    return GetCompaniesResponse(params={LIMIT_QUERY: COMPANIES_AMOUNT}).companies[random.randint(0, COMPANIES_AMOUNT - 1)]


@pytest.fixture
def random_active_company():
    response = GetCompaniesResponse(params={STATUS_QUERY: CompanyStatuses.ACTIVE})
    companies_count = len(response.companies)
    return response.companies[random.randint(0, companies_count - 1)]


@pytest.fixture
def new_user(random_active_company):
    def generate_string(letters_number):
        return "".join(random.choice(string.ascii_letters) for i in range(letters_number))
    first_name = generate_string(5)
    last_name = generate_string(10)
    company_id = random_active_company[Company.Id]
    response = CreateUserResponse(data=json.dumps({ResponseUser.FirstName: first_name, ResponseUser.LastName: last_name,
                                                   ResponseUser.CompanyId: company_id}))
    yield response
    DeleteUserResponse(response.user_id)
