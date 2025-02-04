from django import forms
from roles_user.models import Rol_user

class RolForm(forms.ModelsForm):
    class Meta:
       model = Rol_user
       fields = [
           'rol',
           'usuario',
           
       ]

