from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    objetivo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.usuario.username

class Rutina(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    nivel_dificultad = models.CharField(max_length=50, choices=[("Principiante", "Principiante"), ("Intermedio", "Intermedio"), ("Avanzado", "Avanzado")])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"

class Ejercicio(models.Model):
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE, related_name="ejercicios")
    nombre = models.CharField(max_length=100)
    repeticiones = models.IntegerField()
    series = models.IntegerField()
    descanso = models.IntegerField()
    tiempo_estimado = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.rutina.nombre}"

class RegistroRutina(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return f"{self.usuario.username} - {self.rutina.nombre} ({self.fecha_realizacion})"

class EstadisticasUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    peso_actual = models.FloatField()
    altura_actual = models.FloatField()
    calorias_quemadas = models.IntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha_registro}"

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rutina = models.ForeignKey(Rutina, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rutina.nombre}"