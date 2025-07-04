from django.contrib import admin
from .models import PerfilUsuario, Rutina, Ejercicio, RegistroRutina, EstadisticasUsuario, Comentario

admin.site.register(PerfilUsuario)
admin.site.register(Rutina)
admin.site.register(Ejercicio)
admin.site.register(RegistroRutina)
admin.site.register(EstadisticasUsuario)
admin.site.register(Comentario)