from django import forms
from diagnostico.models import Diagnostico
from cita.models import Cita  # Asegúrate de importar el modelo de Cita
"""
class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['descripcion_diagnostico', 'fecha_diagnostico', 'cita']
        widgets = {
            'fecha_diagnostico': forms.DateInput(attrs={"type": "date"})
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Extraer request si se pasa
        super().__init__(*args, **kwargs)

        # Si el request tiene un id_medico en sesión, filtrar citas
        if request and request.session.get('id_medico'):
            id_medico = request.session.get('id_medico')
            self.fields['cita'].queryset = Cita.objects.filter(medico_id=id_medico)
        else:
            self.fields['cita'].queryset = Cita.objects.all()  # Para el admin
"""
from django import forms
from diagnostico.models import Diagnostico
from cita.models import Cita  # Asegúrate de importar el modelo de Cita

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['descripcion_diagnostico', 'fecha_diagnostico', 'cita']
        widgets = {
            'descripcion_diagnostico': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Escribe la descripción del diagnóstico",
                "rows": 3
            }),
            'fecha_diagnostico': forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),
            'cita': forms.Select(attrs={
                "class": "form-select"
            }),
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Extraer request si se pasa
        super().__init__(*args, **kwargs)

        # Si el request tiene un id_medico en sesión, filtrar citas
        if request and request.session.get('id_medico'):
            id_medico = request.session.get('id_medico')
            self.fields['cita'].queryset = Cita.objects.filter(medico_id=id_medico)
        else:
            self.fields['cita'].queryset = Cita.objects.all()  # Para el admin

        # Aplicar clases de Bootstrap a los campos manualmente
        for field in self.fields:
            if field not in self.Meta.widgets:
                self.fields[field].widget.attrs.update({"class": "form-control"})
