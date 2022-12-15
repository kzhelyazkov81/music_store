from unittest import TestCase
from django.core.exceptions import ValidationError
from music_store.validators import validate_phone_number


class PhoneNumberValidatorTest(TestCase):
    def test_phone_number_validator__when_valid__expect_ok(self):
        validate_phone_number('+359884532332')

    def test_phone_number_validator__when_first_char_is_not_plus_or_zero__expect_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            validate_phone_number('1893567346')

        self.assertIsNotNone(context.exception)

    def test_phone_number_validator__when_char_is_not_digit(self):
        with self.assertRaises(ValidationError) as context:
            validate_phone_number('00359985+940')

        self.assertIsNotNone(context.exception)
