from django.contrib.auth.models import User
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import Profile


class ProfileViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = baker.make(
            User, username="test_username"
        )
        self.profile = baker.make(
            Profile, first_name="test_first_name", last_name="test_last_name"
        )
        self.client = self.client_class()

    def test_create_profile_not_authenticated_user_401(self):
        url = reverse("profile-list")
        response = self.client.post(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_profile_required_fields_400(self):
        url = reverse("profile-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("first_name"), ['This field is required.'])
        self.assertEqual(response.json().get("last_name"), ['This field is required.'])

    def test_create_profile_201(self):
        url = reverse("profile-list")
        self.client.force_authenticate(user=self.user)
        data = {"first_name": "malihe", "last_name": "mz"}
        self.assertEqual(Profile.objects.all().count(), 1)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.all().count(), 2)
        self.assertEqual(Profile.objects.filter(first_name="malihe", last_name="mz").count(), 1)

    def test_list_profile_not_authenticated_user_401(self):
        url = reverse("profile-list")
        response = self.client.get(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_profile_200(self):
        url = reverse("profile-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), Profile.objects.all().count())
        self.assertEqual(response.json()[0].get("id"), self.profile.id)

    def test_profile_detail_not_authenticated_user_401(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        response = self.client.get(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_detail_profile_200(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("id"), self.profile.id)
        self.assertEqual(response.json().get("first_name"), self.profile.first_name)
        self.assertEqual(response.json().get("last_name"), self.profile.last_name)
        self.assertEqual(response.json().get("age"), self.profile.age)
        self.assertEqual(response.json().get("user"), self.profile.user.id)

    def test_destroy_profile_not_authenticated_user_401(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        response = self.client.delete(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_destroy_profile_profile_204(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_profile_not_authenticated_user_401(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        response = self.client.put(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_profile_profile_200(self):
        url = reverse("profile-detail", kwargs={"pk": self.profile.id})
        self.client.force_authenticate(user=self.user)
        data = {
            "first_name": "new_first_name"
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get("id"), self.profile.id)
        self.assertEqual(response.json().get("first_name"), "new_first_name")
        self.assertEqual(response.json().get("last_name"), self.profile.last_name)
        self.assertEqual(response.json().get("age"), self.profile.age)
        self.assertEqual(response.json().get("user"), self.profile.user.id)
