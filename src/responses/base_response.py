from jsonschema.validators import validate
from requests import Response


class BaseResponse:
    def __init__(self, response: Response):
        self.response = response
        self.url = response.request.url
        self.status_code = response.status_code
        self.reason = response.reason
        self.headers = response.headers
        self.response_json = response.json()

    def __str__(self):
        return f"\n{self.url} [{self.status_code} {self.reason}]\n" \
               f"Headers: {self.headers}\n" \
               f"Body: {self.response_json}\n"

    def __repr__(self):
        return f"<{self.url} [{self.status_code} {self.reason}] " \
               f"Headers: {self.headers} " \
               f"Body: {self.response_json}>"

    def validate_against_schema(self, schema):
        print(f"Validate response against JSON schema '{schema}'")
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, (list, tuple, set)):
            print(f"Assert {self.status_code} status code is in {status_code}")
            assert self.status_code in status_code, f"Status code {self.status_code} is not in {status_code}" \
                                                    + self.__str__()
        else:
            print(f"Assert {self.status_code} status code equal to {status_code}")
            assert self.status_code == status_code, f"Status code {self.status_code} is not equal to {status_code}"\
                                                    + self.__str__()
        return self
