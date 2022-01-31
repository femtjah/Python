from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@femtjah.com', password= 'testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """ Probar crear un nuevo usuario con un email correctamente """
        email = 'test@femtjah.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        """ Testea email para nuevo usuario normalizado """ 
        email = 'test@FEMTJAH.COM'
        user = get_user_model().objects.create_user(email,'Testpass123')

        self.assertEqual(user.email , email.lower())

    def test_new_user_invalid_email(self):
        """ Nuevo usuario email invalido """ 
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testpass123')

    def test_create_new_superuser(self):
        """ Crear super usuario creado """
        email = 'test@femtjah.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ probar represemtacion en cadena de texto del tag """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name = 'Billboard Monday'
        )

        self.assertEqual(str(tag),tag.name)

    def test_films_str(self):
        """ Probar representacion en cadena de texto de films """
        films = models.Films.objects.create(
           user=sample_user(),
           title='Spider-Man: No Way Home',
           time_min=120,
           price=14500.00 
        )    

        self.assertEqual(str(films), films.title)
        
    