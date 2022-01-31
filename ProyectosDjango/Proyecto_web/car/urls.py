from django.urls import path

from . import views

app_name='carro'

urlpatterns = [
    
    path('add_car/<int:product_id>/', views.add_product, name='add_car'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_car'),
    path('subtract_prod/<int:product_id>/', views.subtract_prod, name='subtract_prod'),
    path('clean_car/', views.clean_car, name='clean_car'),
]