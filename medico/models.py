

# Create your models here.
from django.db import models
from especialidades.models import Especialidades
from django.contrib.auth.models import User

# Create your models here.
class Medico(models.Model):
    
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Dado de baja', 'Dado de baja'),
    ]
    
    nombre_completo = models.CharField(max_length=50, null=True)
    cedula = models.CharField(max_length=20, null=True)
    correo_electronico = models.EmailField(null=True)
    telefono = models.CharField(max_length=20, null=True)  
    direccion = models.CharField(max_length=100, null=True)
    especialidad=models.ManyToManyField(Especialidades)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='Activo')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre_completo}'
