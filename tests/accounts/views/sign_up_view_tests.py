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
        self.assertEqual(200, response.status_code)
