from datetime import datetime, timezone
import django.contrib.auth.models
from django.db import models
from cita.models import Cita
from medico.models import Medico
from paciente.models import Paciente
from django.contrib.auth.models import User
#from cita.models import Cita


# Create your models here.

class Diagnostico(models.Model):
    
    descripcion_diagnostico = models.TextField(null=True)
    fecha_diagnostico = models.DateField(null=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.fecha_diagnostico} - {self.descripcion_diagnostico}'