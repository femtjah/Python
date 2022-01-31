from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from rest_framework import viewsets, mixins
from rest_framework import authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from core.models import Tag, Films
from Billboard import serializers

class BaseBillboardAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """ Viewsets base """
    authentication_classes = (TokenAuthentication,)
    Permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        """ Retornar objeto para el usuario autenticado """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """ Crear nuevo Objeto """
        serializer.save(user=self.request.user)

class TagviewSet(BaseBillboardAttrViewSet):
    """ Manejar Tags en la base de datos """ 
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

class FilmsviewSet(BaseBillboardAttrViewSet):
    """ Manejar Films en la base de datos """
    queryset = Films.objects.all()
    serializer_class = serializers.FilmsSerializer

    

    