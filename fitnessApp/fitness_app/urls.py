from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django
    path('api/', include('rutinas.urls')),  # Conectar las URLs de la API REST
]