from django import forms
from historialMedico.models import HistorialMedico



class historialMedicoForm(forms.ModelForm):
    class Meta:
       model = HistorialMedico
       fields = [
           'fecha_registro',
           'paciente',
           'medico', 
           'diagnostico',
           'enfermedades_previas',
           
       ]

       widgets = {
           'fecha_registro': forms.DateInput(attrs={"type":"date"})
       }