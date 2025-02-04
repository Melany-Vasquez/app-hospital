from django import forms
from calendarioDisponibilidad.models import CalendarioDisponibilidad
from medico.models import Medico

class CalendarioDisponibilidadForm(forms.ModelForm):
    class Meta:
        model = CalendarioDisponibilidad
        fields = [
            'medico',
            'fecha_inicio',
            'fecha_fin',
        ]
        
        widgets = {
            'medico': forms.Select(attrs={"class": "form form-control mb-2"}),
            'fecha_inicio': forms.DateInput(attrs={"type": "date", "class": "form form-control mb-2"}),
            'fecha_fin': forms.DateInput(attrs={"type": "date", "class": "form form-control mb-2"})
        }
    

    # Validación para evitar la creación de disponibilidad si el médico no está activo
    def clean_medico(self):
        medico = self.cleaned_data['medico']
        if medico.estado != 'Activo':
            raise forms.ValidationError(f'El médico {medico.nombre_completo} no está activo y no se puede crear disponibilidad.')
        return medico


class RangoDisponibilidadForm(forms.Form):
    medico = forms.ModelChoiceField(queryset=Medico.objects.all(), label="Médico")
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de inicio")
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de fin")
    


    # Validación para verificar que el médico esté activo antes de generar la disponibilidad
    def clean_medico(self):
        medico = self.cleaned_data['medico']
        if medico.estado != 'Activo':
            raise forms.ValidationError(f'El médico {medico.nombre_completo} no está activo y no se puede generar disponibilidad.')
        return medico

    # Validación para asegurar que la fecha de inicio sea antes o igual a la fecha de fin
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        return cleaned_data
   
       
