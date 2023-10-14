from src.validation_managers.base_validation_manager import BaseValidationManager


class DeleteUserValidationManager(BaseValidationManager):
    def __init__(self, response):
        super().__init__(response)

