import json
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.test import TestCase
from tienda_api.models import Client


class StoreTestCase(APITestCase):

    def setUp(self):
        Client.objects.create(identification="1720009057", name="Geovanny Alexander", lastname="Merino Romero",
                              email="alexmerino67@gmail.com", phone="0995308851")

    def test_validate_client(self):
        student = Client.objects.get(name="Geovanny Alexander")
        self.assertEqual(str(student.phone),"0995308851")