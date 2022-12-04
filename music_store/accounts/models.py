
from django.db import models
from django.contrib.auth import models as auth_models
from django.core import validators

from music_store.validators import validate_letters_only, validate_phone_number


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_PHONE_NUMBER = 15

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        blank=False,
        null=False,
        help_text='First name',
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters_only,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        blank=False,
        null=False,
        help_text='Last name',
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters_only,
        ),
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
        help_text='Email',
    )

    address = models.TextField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Address',
    )

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE_NUMBER,
        blank=False,
        null=False,
        help_text='Contact phone number',
        validators=(validate_phone_number,)
    )
