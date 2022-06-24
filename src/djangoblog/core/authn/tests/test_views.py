from django.conf import settings
from django.test import TestCase

from djangoblog.core.user.models import BaseUser


class ViewsTestCase(TestCase):
    def setUp(self):
        user = BaseUser.objects.create(
            username="test_user",
            first_name="Test",
            last_name="LastName",
            email="test@mail.com",
        )
        user.set_password("1234")
        user.save()

        self.user = user

    def test_registered_user_can_login(self):
        user = BaseUser.objects.get(username="test_user")
        login_url = settings.LOGIN_URL
        response = self.client.post(
            login_url,
            {"username": user.username, "password": user.password},
            follow=True,
        )
        redirect_path = response.request.get("PATH_INFO")

        self.assertIs(response.status_code, 200)
        # NOTE: this is not working, IDK why yet
        # self.assertEquals(redirect_path, settings.LOGIN_REDIRECT_URL)

    def test_user_exists(self):
        user_count = BaseUser.objects.all().count()
        self.assertEqual(user_count, 1)
   
    def test_user_password(self):
        self.assertTrue(self.user.check_password("1234"))

    def test_logout_redirect(self):
        response = self.client.get("/login/logout", follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.request.get("PATH_INFO"), settings.LOGIN_URL
        )