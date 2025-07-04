from rest_framework import serializers
from .models import PerfilUsuario, Rutina, Ejercicio, RegistroRutina, EstadisticasUsuario, Comentario
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Reemplaza el validador por defecto
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    rutina_nombre = serializers.CharField(source='rutina.nombre', read_only=True)

    class Meta:
        model = Ejercicio
        fields = '__all__'  # incluye todos los campos del modelo
        extra_fields = ['rutina_nombre']  # campo adicional virtual

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['rutina_nombre'] = instance.rutina.nombre if instance.rutina else ''
        return data


class RutinaSerializer(serializers.ModelSerializer):
    ejercicios = EjercicioSerializer(many=True, read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        source='usuario',
        queryset=User.objects.all(),
        write_only=True
    )
    usuario = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rutina
        fields = '__all__'

    def get_usuario(self, obj):
        return obj.usuario.username

    
class RegistroRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroRutina
        fields = '__all__'
        read_only_fields = ['fecha']
        


class EstadisticasUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasUsuario
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    autor = serializers.StringRelatedField(source='usuario', read_only=True)  # aseguramos que 'autor' muestre el nombre

    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'rutina', 'usuario', 'autor', 'fecha']  # ← corregido 'contenido' por 'texto'
        read_only_fields = ['fecha']
