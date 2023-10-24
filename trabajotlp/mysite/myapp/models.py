from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creacion de entidad
class Entidad(models.Model):
    ID = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='entidad_logos/')

    def __str__(self):
        return self.nombre
#creacion de comunicados
class Comunicado(models.Model):
    TIPO_CHOICES = [
        ("S", "Suspensión de actividad"),
        ("C", "Suspensión de clase"),
        ("I", "Información"),
    ]

    titulo = models.CharField(max_length=255)
    detalle = models.CharField(max_length=1000)
    detalle_corto = models.CharField(max_length=255)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField()
    fecha_ultima_modificacion = models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comunicados_publicados")
    modificador_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comunicados_modificados")

    def __str__(self):
        return self.titulo
        
# Relaciónamos user con una entidad
class EntidadAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.user+" "+entidad

    


