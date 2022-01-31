from tabnanny import verbose
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """ Crear y guardar un nuevo Usuario """
        if not email:
            raise ValueError('Los usuarios necesitan un correo')

        user= self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Crear super usuario """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) 

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Modelo personalizado de usurio que soporta hacer login con Email en vez de Usuario """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Movie(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    descrip = models.TextField(max_length=400)
    img = models.ImageField(upload_to='media', null=True, blank=True)

    created= models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta: 
        verbose_name = 'movie'
        verbose_name_plural='movies'

        