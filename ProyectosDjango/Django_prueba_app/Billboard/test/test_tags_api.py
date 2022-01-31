from django.contrib.auth import get_user_model
from django.test.utils import Tag
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from Billboard.serializers import TagSeroalizar

TAGS_URL = reverse('Billboard:tag-list')

class PublicTagsApiTests(TestCase):
    """ Probar los API tags disponibles publicamente """

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """ Prueba que login sea requerido para obtener los tags """
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateTagsApiTests(TestCase):
    """ Probar los API tags disponibles provados """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@dfemtjah.com',
            'password'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """ Probar obtener tags """
        Tag.objects.create(user=self.user, name='Batman')
        Tag.objects.create(user=self.user, name='Superman')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('name')
        serializer = TagSeroalizar(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """ Probar que los tags retornados sean del usuarios """
        user2 = get_user_model().objects.create_user(
            'otro@femtjah.com',
            'testpass'
        )
        Tag.objects.create(user=user2, name='Flash')
        tag = Tag.objects.create(user = self.user, name='Waterman')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag_successful(self):
        """ Prueba creando nuevo tag """
        payload = {'name': 'Simple'}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """ Prueba crear un nuevo tag con un payload invalido """
        payload = {'name': ''}
        res = self.client.post(TAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)