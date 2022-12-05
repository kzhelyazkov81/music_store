from django.db import models

from music_store.validators import validate_file_size


class Accessory(models.Model):
    MAX_CHAR_LENGTH = 50
    STRINGS = 'Strings'
    PICK = 'Pick'
    CYMBAL = 'Cymbal'
    DRUM = 'Drum'
    TYPES = (
        (STRINGS, STRINGS),
        (PICK, PICK),
        (CYMBAL, CYMBAL),
        (DRUM, DRUM),
    )

    type = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        choices=TYPES,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        blank=False,
        null=False,
    )

    dimension = models.CharField(
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
        return f'{self.type} - {self.model}'

