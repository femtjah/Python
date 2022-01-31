from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers

from core.models import Tag, Films

class TagSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Tag """
    class Meta: 
        models = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class FilmsSerializer(serializers.ModelSerializer):
    """ Serializador para objeto de Films """
    class Meta: 
        models = Films
        fields = ('id', 'name')
        read_only_Fields = ('id',)        
        