          

from django import forms
from .models import Cita, Medico
from datetime import time
from especialidades.models import Especialidades
HOUR_CHOICES = [
    (time(hour=9, minute=0), '09:00'),
    (time(hour=9, minute=30), '09:30'),
    (time(hour=10, minute=0), '10:00'),
    (time(hour=10, minute=30), '10:30'),
    (time(hour=11, minute=0), '11:00'),
    (time(hour=11, minute=30), '11:30'),
    (time(hour=13, minute=30), '13:30'),
    (time(hour=14, minute=0), '14:00'),
    (time(hour=14, minute=30), '14:30'),
    (time(hour=15, minute=0), '15:00'),
    (time(hour=15, minute=30), '15:30'),
    (time(hour=16, minute=0), '16:00'),
    ('emergency', 'Emergencia'),  # Opción de emergencia
]

class CitaForm(forms.ModelForm):
    
    # Especialidad con widget de selección y estilo de Bootstrap
    especialidad = forms.ChoiceField(
        choices=[(especialidad.id, especialidad.nombre_especialidad) for especialidad in Especialidades.objects.all()],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione una especialidad'})
    )

    fecha_cita = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    hora_cita = forms.ChoiceField(
        choices=HOUR_CHOICES,
        required=True,
        label='Hora de la cita',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Cambiar estado_covid a un campo de selección
    estado_covid = forms.ChoiceField(
        choices=Cita.COVID_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Campo atendida (casillero de selección)

    atendida = forms.BooleanField(
    required=False,
    widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )

    class Meta:
        model = Cita
        fields = ['fecha_cita', 'especialidad', 'medico', 'paciente', 'descripcion', 'estado_covid', 'hora_cita', 'atendida']

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        
        self.fields['medico'].widget.attrs.update({'class': 'form-control'})
        self.fields['paciente'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'rows': '3'})


class CitaForm_medico (forms.ModelForm):
    
    especialidad = forms.ChoiceField(
        choices=[(especialidad.id, especialidad.nombre_especialidad) for especialidad in Especialidades.objects.all()],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione una especialidad'})
    )

    fecha_cita = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    hora_cita = forms.ChoiceField(
        choices=HOUR_CHOICES,
        required=True,
        label='Hora de la cita',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Cambiar estado_covid a un campo de selección
    estado_covid = forms.ChoiceField(
        choices=Cita.COVID_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Campo atendida (casillero de selección)

    atendida = forms.BooleanField(
    required=False,
    widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )

    class Meta:
        model = Cita
        fields = ['fecha_cita', 'especialidad', 'medico', 'paciente', 'descripcion', 'estado_covid', 'hora_cita', 'atendida']

    def __init__(self, *args, id_medico = None, **kwargs):
        super(CitaForm_medico, self).__init__(*args, **kwargs)
        especialidades = []  # Definir la variable antes de usarla
        # Aplicar clases CSS de Bootstrap a otros campos
        #self.fields['medico'].widget.attrs.update({'class': 'form-control'})
        if id_medico:
            self.fields['medico'].initial = id_medico
            medico = Medico.objects.get(id=id_medico)
            especialidades = medico.especialidad.all()
            
        if especialidades:
            self.fields['especialidad'] = forms.ChoiceField(
                choices=[(especialidad.id, especialidad.nombre_especialidad) for especialidad in especialidades],
                required=True,
                widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione una especialidad'})
            )
        
        self.fields['medico'].widget.attrs.update({'class': 'form-control', 'style': 'pointer-events: none; background-color: #e9ecef;'})
        self.fields['paciente'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})


        
class CitaForm_paciente (forms.ModelForm):
    
    especialidad = forms.ChoiceField(
        choices=[(especialidad.id, especialidad.nombre_especialidad) for especialidad in Especialidades.objects.all()],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione una especialidad'})
    )

    fecha_cita = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    hora_cita = forms.ChoiceField(
        choices=HOUR_CHOICES,
        required=True,
        label='Hora de la cita',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Cambiar estado_covid a un campo de selección
    estado_covid = forms.ChoiceField(
        choices=Cita.COVID_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Campo atendida (casillero de selección)

    atendida = forms.BooleanField(
    required=False,
    widget=forms.CheckboxInput(attrs={'class': 'custom-checkbox'})
    )

    class Meta:
        model = Cita
        fields = ['fecha_cita', 'especialidad', 'medico', 'paciente', 'descripcion', 'estado_covid', 'hora_cita', 'atendida']

    def __init__(self, *args, id_paciente = None, **kwargs):
        super(CitaForm_paciente, self).__init__(*args, **kwargs)
        # Aplicar clases CSS de Bootstrap a otros campos
        #self.fields['medico'].widget.attrs.update({'class': 'form-control'})
        if id_paciente:
            self.fields['paciente'].initial = id_paciente
            
            
        self.fields['medico'].widget.attrs.update({'class': 'form-control'})
        self.fields['paciente'].widget.attrs.update({'class': 'form-control',  'style': 'pointer-events: none; background-color: #e9ecef;'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control'})
        
