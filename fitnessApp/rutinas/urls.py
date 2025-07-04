from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PerfilUsuarioViewSet, RutinaViewSet,
    EjercicioViewSet, RegistroRutinaViewSet, EstadisticasUsuarioViewSet, ComentarioViewSet
)

# Configurar el enrutador para gestionar automáticamente los endpoints de la API
router = DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'perfiles', PerfilUsuarioViewSet, basename='perfiles')
router.register(r'rutinas', RutinaViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'registro-rutina', RegistroRutinaViewSet)
router.register(r'estadisticas', EstadisticasUsuarioViewSet, basename='estadisticas')
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Expone todas las rutas automáticamente
]