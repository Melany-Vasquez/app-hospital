from django.db import models
from diagnostico.models import Diagnostico
from medico.models import Medico
from paciente.models import Paciente
from django.utils import timezone

# Create your models here.

class Receta(models.Model):
    
    fecha_registro = models.DateField(default=timezone.now, null=True)
    #medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True)
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    descripcion_receta = models.TextField(null=True)
    medicacion_nombre = models.CharField(max_length=255, null=True, blank=True)  # Ej: "Paracetamol"
    medicacion_dosis = models.CharField(max_length=100, null=True, blank=True)   # Ej: "500 mg"
    medicacion_frecuencia = models.CharField(max_length=100, null=True, blank=True)  # Ej: "Cada 8 horas"
    medicacion_duracion = models.CharField(max_length=100, null=True, blank=True)  # Ej: "5 días"

    @property
    def medico(self):
        """Obtiene el médico a través del diagnóstico y la cita"""
        return self.diagnostico.cita.medico
    
    def __str__(self):
        return f'Receta del {self.paciente} - {self.fecha_registro} - {self.diagnostico}'
    