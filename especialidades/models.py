from django.db import models
from django.utils import timezone

# Create your models here.
class Especialidades(models.Model):
    
    nombre_especialidad = models.CharField(max_length=50,null=True)
    descripcion_especialidad = models.TextField(null=True)
    fecha_registro = models.DateField(null=True)
    
    

    def __str__(self):
        return self.nombre_especialidad
    