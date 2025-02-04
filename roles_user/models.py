from django.db import models
from django.contrib.auth.models import User

class Rol_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    rol= models.CharField(max_length=25),
    
    def __str__(self):
        return f'Cita de  con {self.rol}'     

# Create your models here.
