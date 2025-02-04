import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    nombre_completo=models.CharField(max_length=150)
    cedula=models.CharField(max_length=15)
    fecha_nacimiento=models.DateField(null=True)
    direccion=models.CharField(max_length=250)
    telefono=models.CharField(max_length=15)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=True)
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nombre_completo}'
    
    
    
    
    
        
