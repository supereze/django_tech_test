# coding: utf8
from django.urls import reverse
from rest_framework.test import APITestCase
from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory


class LocationCreateTest(APITestCase):

    url = reverse("locations:v1_list_create_location")
    urlGet = reverse("locations:v1_get_put_delete_location", args=['loc_20181213221341a12e4b4f'])

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)

    def test_get_successfully(self):
        response = self.client.get(self.urlGet)
        response = response.json()

        self.assertEquals(response.status_code, 201)

    def test_update_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.put(self.urlGet, data, format='json')
        self.assertEquals(response.status_code, 201)

    def test_destroy_successfully(self):

        response = self.client.delete(self.urlGet)
        response = response.json()

        self.assertEquals(response.status_code, 204)
