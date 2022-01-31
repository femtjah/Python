from django import urls
from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from Billboard import views

router = DefaultRouter()
router.register('tags', views.TagviewSet)
router.register('films', views.FilmsviewSet)

app_name = 'Billboard'

urlpatterns = [
    path('', include(router.urls))

]