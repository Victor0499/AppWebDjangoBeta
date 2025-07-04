from rutinas.models import Rutina, Ejercicio
from django.contrib.auth.models import User


usuario, creado = User.objects.get_or_create(username="victor_prueba")


rutina = Rutina.objects.create(
    usuario=usuario,
    nombre="Entrenamiento intensivo",
    descripcion="Rutina enfocada en fuerza y resistencia",
    duracion=60,
    nivel_dificultad="Avanzado"
)


Ejercicio.objects.create(rutina=rutina, nombre="Sentadillas", repeticiones=12, series=3, descanso=30, tiempo_estimado=60)
Ejercicio.objects.create(rutina=rutina, nombre="Flexiones", repeticiones=15, series=4, descanso=30, tiempo_estimado=60)

Rutina.objects.all()  
Ejercicio.objects.all()  


for r in Rutina.objects.all():
    print(f"{r.nombre} – {r.usuario.username}")


duplicada = Rutina.objects.filter(nombre="Entrenamiento intensivo", usuario__username="victor_prueba")[0]
duplicada.delete()
