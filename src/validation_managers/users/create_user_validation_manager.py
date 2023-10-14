from src.validation_managers.users.base_user_validation_manager import BaseUserValidationManager


class CreateUserValidationManager(BaseUserValidationManager):
    def __init__(self, response):
        super().__init__(response)
