from django.urls import path

from films import views



urlpatterns = [
    path('movies/', views.MovieViewSet, mane ='movies'),
    
]
