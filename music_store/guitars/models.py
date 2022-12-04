
from django.db import models

from music_store.validators import validate_file_size, validate_strings_number


class Guitar(models.Model):
    MAX_CHAR_LENGTH = 50
    ACOUSTIC = 'Acoustic'
    ELECTRIC = 'Electric'
    BASS = 'Bass'
    TYPES = (
        (ACOUSTIC, ACOUSTIC),
        (ELECTRIC, ELECTRIC),
        (BASS, BASS),
    )
    type = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        choices=TYPES,
    )
    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )
    fretboard = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )
    body = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )
    strings = models.PositiveIntegerField(
        validators=(validate_strings_number,),
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
