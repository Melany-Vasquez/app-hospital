from django.db import models
from medico.models import Medico

# Create your models here.

class CalendarioDisponibilidad(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    #hora_inicio = models.TimeField(null=True)
    #hora_fin = models.TimeField(null=True) 
    #es_emergencia = models.BooleanField(default=False)  

    def __str__(self):
        return f'Disponibilidad de {self.medico} el {self.fecha_inicio} al {self.fecha_fin}'
