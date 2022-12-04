from django.db import models

from music_store.validators import validate_keys_number, validate_file_size


class Keyboard(models.Model):
    MAX_CHAR_LENGTH = 50

    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    keys = models.PositiveIntegerField(
        validators=(validate_keys_number,),
        blank=False,
        null=False,
    )

    sounds = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    image = models.ImageField(
        upload_to='images',
        validators=(validate_file_size,),
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.model
