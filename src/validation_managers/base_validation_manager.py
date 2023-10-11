from jsonschema.validators import validate


class BaseValidationManager:
    def __init__(self, response):
        self.response = response

    def __str__(self): self.response.__str__()

    def schema_equals(self, schema):
        print(f"Validate response against JSON schema '{schema}'")
        if isinstance(self.response.response_json, list):
            for item in self.response.response_json:
                validate(item, schema)
        else:
            validate(self.response.response_json, schema)
        return self.response

    def status_code_equals(self, status_code):
        if isinstance(status_code, (list, tuple, set)):
            print(f"Assert {self.response.status_code} status code is in {status_code}")
            assert self.response.status_code in status_code, \
                f"Status code {self.response.status_code} is not in {status_code}" + self.response.__str__()
        else:
            print(f"Assert {self.response.status_code} status code equal to {status_code}")
            assert self.response.status_code == status_code, \
                f"Status code {self.response.status_code} is not equal to {status_code}" + self.response.__str__()
        return self.response
