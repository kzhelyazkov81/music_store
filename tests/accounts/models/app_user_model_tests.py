from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

UserModel = get_user_model()


class AppUserModelTests(TestCase):
    def test_app_user_save__when_first_last_name_and_phone_are_valid__expect_correct_result(self):
        user = UserModel(
            username='kzz',
            email='kkk@mail.com',
            first_name='kolyo',
            last_name='zhelyazkov',
            address='asdf',
            phone_number='0095832455',
            password='!zaq2wsx'
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user.pk)

    def test_app_user_save__when_first_name_is_not_valid__expect_exception(self):
        user = UserModel(
            username='kzz',
            email='kkk@mail.com',
            first_name='k1olyo',
            last_name='zhelyazkov',
            address='asdf',
            phone_number='0095832455',
            password='!zaq2wsx'
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_app_user_save__when_last_name_is_not_valid__expect_exception(self):
        user = UserModel(
            username='kzz',
            email='kkk@mail.com',
            first_name='kolyo',
            last_name='1zhelyazkov',
            address='asdf',
            phone_number='0095832455',
            password='!zaq2wsx'
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_app_user_save__when_phone_number_is_not_valid__expect_exception(self):
        user = UserModel(
            username='kzz',
            email='kkk@mail.com',
            first_name='kolyo',
            last_name='zhelyazkov',
            address='asdf',
            phone_number='8095832455',
            password='!zaq2wsx'
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)
