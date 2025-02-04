from django.db import models
from diagnostico.models import Diagnostico
from medico.models import Medico
from paciente.models import Paciente

# Create your models here.

class HistorialMedico(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_registro = models.DateField(null=True)  # Registro automático de la fecha de creación
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    diagnostico = models.ManyToManyField(Diagnostico, related_name='historiales')
    enfermedades_previas = models.CharField(null=True, max_length=255)

    def __str__(self):
        return f'Historial de {self.paciente} - {self.fecha_registro}'
    
    def obtener_diagnosticos(self):
        return self.diagnosticos.all().order_by('fecha_diagnostico')   