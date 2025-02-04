
from django.shortcuts import get_object_or_404, redirect, render
from diagnostico.forms import DiagnosticoForm
from diagnostico.models import Diagnostico
from django.contrib.auth.decorators import login_required

from inicio.views import login_required_and_check_session


def lista_diagnostico(request):
    tipo_usuario = request.session['tipo_usuario']  # Obtener el tipo de usuario desde la sesión

    if tipo_usuario == 'Admin':
        diagnosticos = Diagnostico.objects.all()  # Si es Admin, mostrar todos los diagnósticos
        return render(request, 'diagnostico/lista_diagnostico.html', {'diagnostico': diagnosticos})

    if tipo_usuario == 'Paciente':
        id_paciente = request.session['id_paciente']  # Obtener el ID del paciente desde la sesión
        diagnosticos = Diagnostico.objects.filter(cita__paciente_id=id_paciente)  # Filtrar los diagnósticos por el paciente
        return render(request, 'diagnostico/lista_diagnostico_paciente.html', {'diagnostico': diagnosticos})

    if tipo_usuario == 'Medico':
        id_medico = request.session['id_medico']  # Obtener el ID del médico desde la sesión
        diagnosticos = Diagnostico.objects.filter(cita__medico_id=id_medico)  # Filtrar los diagnósticos por el médico
        return render(request, 'diagnostico/lista_diagnostico_medico.html', {'diagnostico': diagnosticos})

    

@login_required
def crear_diagnostico(request):
    if request.method == 'POST': 
        form= DiagnosticoForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("lista_diagnostico")
        else:
            return render(request, 'diagnostico/crear_diagnostico.html', {'form': form})
    else:
        form = DiagnosticoForm()
        return render(request, 'diagnostico/crear_diagnostico.html', {'form': form})

@login_required
def editar_diagnostico(request, diagnostico_id):
    diagnostico=get_object_or_404(Diagnostico, id=diagnostico_id)
    if request.method ==  'POST':
        form= DiagnosticoForm(request.POST,  instance=diagnostico)

        if form.is_valid(): 
            form.save()
            return redirect("lista_diagnostico")
        else:
            return render(request, 'diagnostico/crear_diagnostico.html', {'form': form})
    else:
        form = DiagnosticoForm(instance=diagnostico)
        return render(request, 'diagnostico/crear_diagnostico.html', {'form': form})
    
@login_required
def eliminar_diagnostico(request, diagnostico_id):
    diagnostico=get_object_or_404(Diagnostico, id=diagnostico_id)
    if request.method ==  'POST':
        diagnostico.delete()
        return redirect("lista_diagnostico")
    else:
        return render(request, 'diagnostico/eliminar_diagnostico.html', {'diagnostico': diagnostico})
    
"""
@login_required
def lista_diagnostico_paciente(request):
    # Filtra los diagnósticos para que solo se muestren los del usuario logueado
    diagnosticos = Diagnostico.objects.filter(user_id=request.user)
    return render(request, 'diagnostico/lista_diagnostico_paciente.html', {'diagnosticos': diagnosticos})
"""
    
def crear_diagnostico_medico(request):
    if request.method == 'POST': 
        # Pasa el request al formulario
        form = DiagnosticoForm(request.POST, request=request)  # Asegúrate de pasar el request aquí
        if form.is_valid(): 
            form.save()
            return redirect("lista_diagnostico")  # Redirige después de guardar
        else:
            return render(request, 'diagnostico/crear_diagnostico_medico.html', {'form': form})
    else:
        # Pasa el request al formulario también en GET
        form = DiagnosticoForm(request=request)  # Pasa el request aquí también
        return render(request, 'diagnostico/crear_diagnostico_medico.html', {'form': form})
    
def lista_diagnostico_medico(request):
    tipo_usuario = request.session['tipo_usuario']  # Obtener el tipo de usuario desde la sesión

    if tipo_usuario == 'Admin':
        diagnosticos = Diagnostico.objects.all()  # Si es Admin, mostrar todos los diagnósticos
        return render(request, 'diagnostico/lista_diagnostico.html', {'diagnostico': diagnosticos})

    if tipo_usuario == 'Paciente':
        id_paciente = request.session['id_paciente']  # Obtener el ID del paciente desde la sesión
        diagnosticos = Diagnostico.objects.filter(cita__paciente_id=id_paciente)  # Filtrar los diagnósticos por el paciente
        return render(request, 'diagnostico/lista_diagnostico_paciente.html', {'diagnostico': diagnosticos})

    if tipo_usuario == 'Medico':
        id_medico = request.session['id_medico']  # Obtener el ID del médico desde la sesión
        diagnosticos = Diagnostico.objects.filter(cita__medico_id=id_medico)  # Filtrar los diagnósticos por el médico
        return render(request, 'diagnostico/lista_diagnostico_medico.html', {'diagnostico': diagnosticos})    
