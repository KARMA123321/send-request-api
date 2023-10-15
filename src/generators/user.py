import random

from faker import Faker

import config
from src.enums.schemas.schemas_keys.response_user import ResponseUser


class User:

    def __init__(self):
        self.fake = Faker()
        self.result = {}

    def set_first_name(self, first_name):
        self.result[ResponseUser.FirstName] = first_name
        return self

    def set_last_name(self, last_name):
        self.result[ResponseUser.LastName] = last_name
        return self

    def set_company_id(self, company_id):
        self.result[ResponseUser.CompanyId] = company_id
        return self

    def populate(self):
        return self.set_first_name(self.fake.first_name())\
            .set_last_name(self.fake.last_name())\
            .set_company_id(random.randint(1, config.COMPANIES_AMOUNT))

    def build(self):
        return self.result
