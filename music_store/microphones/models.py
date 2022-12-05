from django.db import models

from music_store.validators import validate_file_size


class Microphone(models.Model):
    MAX_CHAR_LENGTH = 50
    VOCAL = 'Vocal'
    INSTRUMENTAL = 'Instrumental'
    TYPES = (
        (VOCAL, VOCAL),
        (INSTRUMENTAL, INSTRUMENTAL),
    )

    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    type = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        choices=TYPES,
    )

    frequency = models.CharField(
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

    def __str__(self):
        return self.model

