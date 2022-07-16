from django.contrib.auth import get_user_model
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from caterings.models import Catering


class MachineTestAPIView(APITestCase):

    def test_get_retrieve(self):
        catering = mixer.cycle(5).blend(Catering)
        url = reverse('caterings-list')
        factory = APIRequestFactory()
        request = factory.get(url)
        force_authenticate(request)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
