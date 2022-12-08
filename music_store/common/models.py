from django.db import models

from music_store.validators import validate_phone_number


class Order(models.Model):
    MAX_CHAR_LENGTH = 50
    MAX_LEN_PHONE_NUMBER = 15

    article = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    quantity = models.PositiveIntegerField(
        default=1,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    address = models.TextField(
        max_length=100,
        blank=False,
        null=False,
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE_NUMBER,
        blank=False,
        null=False,
        help_text='Contact phone number',
        validators=(validate_phone_number,)
    )

    def __str__(self):
        return f'{self.id} - {self.article}'
