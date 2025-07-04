from rest_framework import viewsets
from .models import PerfilUsuario, Rutina, Ejercicio, RegistroRutina, EstadisticasUsuario, Comentario
from .serializers import (
    PerfilUsuarioSerializer,
    RutinaSerializer,
    EjercicioSerializer,
    RegistroRutinaSerializer,
    EstadisticasUsuarioSerializer,
    ComentarioSerializer
)
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilUsuarioSerializer

    def get_queryset(self):
        queryset = PerfilUsuario.objects.all()
        usuario_id = self.request.query_params.get('usuario')
        if usuario_id:
            queryset = queryset.filter(usuario__id=usuario_id)
        return queryset

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class RegistroRutinaViewSet(viewsets.ModelViewSet):
    queryset = RegistroRutina.objects.all()
    serializer_class = RegistroRutinaSerializer

class EstadisticasUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = EstadisticasUsuarioSerializer

    def get_queryset(self):
        queryset = EstadisticasUsuario.objects.all().order_by('-fecha_registro')
        usuario_id = self.request.query_params.get('usuario')
        if usuario_id:
            queryset = queryset.filter(usuario__id=usuario_id)
        return queryset
    
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer