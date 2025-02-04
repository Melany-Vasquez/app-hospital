from django import forms
from .models import Especialidades

class EspecialidadesForm(forms.ModelForm):
    class Meta:
       model = Especialidades
       fields = [
           'nombre_especialidad',
           'descripcion_especialidad',
           'fecha_registro', 
       ]

       widgets = {
            'fecha_registro': forms.DateInput(attrs={"type":"date",  "class":"form-control"}),
            'nombre_especialidad':  forms.TextInput(attrs={"class":"form-control"}),
            'descripcion_especialidad':  forms.Textarea(attrs={"class":"form-control"}),
       }
            