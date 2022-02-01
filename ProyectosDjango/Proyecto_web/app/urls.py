from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('service.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('store/', include('store.urls')),
    path('carro/', include('car.urls')),
    path('', include('core.urls')),
    path('authentication/', include('authentication.urls')),

]
