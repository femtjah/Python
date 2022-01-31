from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers

from core.models import Movie


class FilmsSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Films """
    class Meta: 
        model = Movie
        fields = ('id', 'name')
        read_only_Fields = ('id',)     