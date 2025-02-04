from django import forms
from medico.models import Medico
from especialidades.models import Especialidades

class MedicoForm(forms.ModelForm):
    # Campos personalizados
    nombre_completo = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'})
    )
    cedula = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula'})
    )
    correo_electronico = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    telefono = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'})
    )
    direccion = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'})
    )
    especialidad = forms.ModelMultipleChoiceField(
        queryset=Especialidades.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label="Especialidades"
    )
    estado = forms.ChoiceField(
        choices=Medico.ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Estado del médico"
    )

    class Meta:
        model = Medico
        fields = [
            'nombre_completo',
            'cedula',
            'correo_electronico',
            'telefono',
            'direccion',
            'especialidad',
            'estado',
        ]
