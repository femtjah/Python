from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Films

from Billboard.serializers import FilmsSerializer

FILMS_URL = reverse('Billboard:films-list')

class PublicFilmsApiTests(TestCase):
    """ Probar los API Films disponibles publicamente """
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """ Prueba que login sea requerido para obtener los Films """
        res = self.client.get(FILMS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)



class PrivateFilmsApiTests(TestCase):
    """ Probar los API Films disponibles publicamente """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@dfemtjah.com',
            'password'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_films_list(self):
        """ Probar obtener lista de peliculas """
        Films.objects.create(user=self.user, name='Batman')
        Films.objects.create(user=self.user, name='Superman')

        res = self.client.get(FILMS_URL)

        films = Films.objects.all().order_by('-name')
        serializer = FilmsSerializer(films, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_films_limited_to_user(self):
        """ Probar que los films retornados sean del usuarios """
        user2 = get_user_model().objects.create_user(
            'otro@femtjah.com',
            'testpass'
        )
        Films.objects.create(user=user2, name='Flash')
        films = Films.objects.create(user = self.user, name='Waterman')

        res = self.client.get(FILMS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], films.name)

    def test_create_films_successful(self):
        """ Prueba creando nuevo films """
        payload = {'name': 'Suicide Squad'}
        self.client.post(FILMS_URL, payload)

        exists = Films.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_films_invalid(self):
        """ Prueba crear un nuevo films con un payload invalido """
        payload = {'name': ''}
        res = self.client.post(FILMS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)