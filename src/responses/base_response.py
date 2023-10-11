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
