from django.contrib.auth import get_user_model
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

User = get_user_model()


class MachineTestAPIView(APITestCase):

    def setUp(self):
        self.simple_user = mixer.blend(User)

    def test_get_retrieve(self):
        user = mixer.cycle(5).blend(User)
        url = reverse('users-list')
        factory = APIRequestFactory()
        request = factory.get(url)
        force_authenticate(request)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
