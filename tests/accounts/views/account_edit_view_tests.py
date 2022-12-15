from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class SignUpViewTest(TestCase):
    def test_sign_up__when_anonymous_user__expect_create_account(self):
        credentials = {
            'username': 'username',
            'email': 'some@mail.com',
            'password': '!zaq2wsx',
        }

        UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.post(
            reverse('create'),
            data=credentials,
        )

        self.assertEqual(credentials['username'], response.context['user'].username)


class AccountEditViewTest(TestCase):
    def test_edit_account__when_user_is_logged_in__expect_edit_account(self):
        profile_data = {
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'some@mail.com',
            'address': 'address',
            'phone_number': '00359854356',
        }

        credentials = {
            'username': 'username',
            'email': 'some@mail.com',
            'password': '!zaq2wsx',
        }

        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.post(
            reverse('edit profile', kwargs={'pk': user.pk}),
            data=profile_data,
        )

        created_profile = UserModel.objects.filter(**profile_data).get()
        self.assertIsNotNone(created_profile)
        self.assertEqual(302, response.status_code)
