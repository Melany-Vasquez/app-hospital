from datetime import timedelta
from django.db import models

from calendarioDisponibilidad.models import CalendarioDisponibilidad
from medico.models import Medico
from paciente.models import Paciente

# Create your models here.

class Cita(models.Model):
    
    COVID_CHOICES = [
        ('S', 'Presenta síntomas'),
        ('N', 'No presenta síntomas'),
    ]
    
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True )  # O un modelo relacionado de pacientes
    fecha_cita = models.DateField(null=True )
    descripcion = models.TextField(null=True)
    estado_covid = models.CharField(max_length=1, choices=COVID_CHOICES, default='N')
    cita_duracion = models.DurationField(default=timedelta(minutes=30)) 
    hora_cita = models.TimeField(null=True)  # Campo para la hora de la cita
    atendida = models.BooleanField(default=False)  # Campo para marcar si la cita fue atendida

    def __str__(self):
        return f'Cita de {self.paciente} con {self.medico}'   
    