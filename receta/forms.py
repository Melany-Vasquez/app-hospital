from django import forms
from receta.models import Receta
from diagnostico.models import Diagnostico  # Importa tu modelo de diagnóstico

class RecetaForm(forms.ModelForm):
    fecha_registro = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    diagnostico = forms.ModelChoiceField(
        queryset=Diagnostico.objects.none(),  # Se inicializa vacío y se llena en __init__
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un diagnóstico"
    )
    descripcion_receta = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    medicacion_nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    medicacion_dosis = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    medicacion_frecuencia = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    medicacion_duracion = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Receta
        fields = [
            'fecha_registro',
            'diagnostico',
            'descripcion_receta',
            'medicacion_nombre',
            'medicacion_dosis',
            'medicacion_frecuencia',
            'medicacion_duracion',
        ]

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Extrae el request si se pasó
        super().__init__(*args, **kwargs)

        if request and request.session.get('id_medico'):
            id_medico = request.session.get('id_medico')
            self.fields['diagnostico'].queryset = Diagnostico.objects.filter(cita__medico_id=id_medico)
