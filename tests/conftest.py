import json
import random
import string

import allure
import pytest

from config import COMPANIES_AMOUNT
from src.enums.company_statuses import CompanyStatuses
from src.enums.schemas.schemas_keys.company import Company
from src.enums.schemas.schemas_keys.response_user import ResponseUser
from src.generators.user import User
from src.responses.companies.get_companies_response import GetCompaniesResponse, LIMIT_QUERY, STATUS_QUERY
from src.responses.users.create_user_response import CreateUserResponse
from src.responses.users.delete_user_response import DeleteUserResponse


@allure.title("Get random company")
@pytest.fixture
def random_company():
    return GetCompaniesResponse(params={LIMIT_QUERY: COMPANIES_AMOUNT}).companies[random.randint(0, COMPANIES_AMOUNT - 1)]


@allure.title("Get random active company")
@pytest.fixture
def random_active_company():
    response = GetCompaniesResponse(params={STATUS_QUERY: CompanyStatuses.ACTIVE})
    companies_count = len(response.companies)
    return response.companies[random.randint(0, companies_count - 1)]


@allure.title("Create new user and get response")
@pytest.fixture
def new_user(random_active_company, faker):
    with allure.step("Create new user"):
        user = User().populate().set_company_id(random_active_company[Company.Id]).build()
        response = CreateUserResponse(data=json.dumps(user))

    yield response

    with allure.step("Delete new user"):
        DeleteUserResponse(response.user_id)
