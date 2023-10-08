from jsonschema.validators import validate
from requests import Response


class BaseResponse:
    def __init__(self, response: Response):
        self.response = response
        self.url = response.request.url
        self.status_code = response.status_code
        self.reason = response.reason
        self.response_json = response.json()

    def __str__(self): return f"Response {self.url} [{self.status_code} {self.reason}]"

    def __repr__(self): return f"<{self.url} [{self.status_code} {self.reason}]>"

    def validate_against_schema(self, schema):
        print(f"Validate response against JSON schema '{schema}'")
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, (list, tuple, set)):
            print(f"Assert {self.status_code} status code is in {status_code}")
            assert self.status_code in status_code, f"Status code {self.status_code} is not in {status_code}"
        else:
            print(f"Assert {self.status_code} status code equal to {status_code}")
            assert self.status_code == status_code, f"Status code {self.status_code} is not equal to {status_code}"

        return self
