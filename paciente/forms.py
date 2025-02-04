from django import forms
from paciente.models import Paciente

class PacienteForm(forms.ModelForm):

    nombre_completo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    cedula = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    genero = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Femenino')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
       model = Paciente
       fields = [
           'nombre_completo',
           'cedula',
           'fecha_nacimiento', 
           'direccion',
           'telefono',
           'genero',
           
       ]
        
       widgets = {
           'fecha_nacimiento': forms.DateInput(attrs={"type":"date"})
       }