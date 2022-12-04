from django.db import models

from music_store.validators import validate_file_size


class DrumSet(models.Model):
    MAX_CHAR_LENGTH = 50

    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    bass = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    floor = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    first_tom = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=True,
        null=True,
    )

    second_tom = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=True,
        null=True,
    )

    third_tom = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=True,
        null=True,
    )

    body_material = models.CharField(
        max_length=MAX_CHAR_LENGTH,
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
