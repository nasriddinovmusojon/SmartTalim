import re
from django.core.exceptions import ValidationError

UZ_PHONE_REGEX = re.compile(
    r'^(?:\+998|998|0)?(90|91|93|94|95|97|98|99|33|88|77|70|20|71)\d{7}$'
)

def uz_phone_validator(value: str):
    value = value.replace(" ", "").replace("-", "")
    if not UZ_PHONE_REGEX.match(value):
        raise ValidationError(
            "Telefon raqam notog'ri kiritilgan. 998-90-123-45-67 holatida bo'lsin"
        )