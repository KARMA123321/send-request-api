import allure
from jsonderef import JsonDeref

import pytest
import requests


@allure.title("Get JSON-schemas from OpenAPI spec")
@pytest.fixture(scope="session")
def schemas():
    spec = requests.get("https://send-request.me/openapi.json")
    deref_spec = JsonDeref().deref(spec.json(), 1000)
    yield deref_spec["components"]["schemas"]
