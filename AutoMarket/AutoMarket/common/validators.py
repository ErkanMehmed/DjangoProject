from datetime import date
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FoundedYearValidator:
    def __init__(self, message: str):
        self.message = message

    def __call__(self, value):
        current_year = date.today().year

        if value < 1800 or value > current_year:
            raise ValidationError(self.message, code="invalid_year")
