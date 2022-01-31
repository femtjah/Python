from rest_framework.serializers import Serializer
from django.shortcuts import render

from core.models import Movie
from films import serializers

class MovieViewSet(serializers.FilmsSerializer):
    queryset = Movie.objects.all()
    serializer_class = serializers.FilmsSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def films_create (self, serializer):
        serializer.save(user=self.request.user)
