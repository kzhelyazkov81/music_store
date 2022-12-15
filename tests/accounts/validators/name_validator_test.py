from unittest import TestCase
from django.core.exceptions import ValidationError
from music_store.validators import validate_letters_only


class NameValidatorTest(TestCase):
    def test_name_validator__when_valid__expect_ok(self):
        validate_letters_only('Username')

    def test_name_validator__when_name_contains_digit__expect_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            validate_letters_only('User1')

        self.assertIsNotNone(context.exception)

    def test_name_validator__when_name_contains_symbols__expect_validation_error(self):
        with self.assertRaises(ValidationError) as context:
            validate_letters_only('User_')

        self.assertIsNotNone(context.exception)
