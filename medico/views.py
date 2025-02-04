import django.contrib.auth.models
from django.shortcuts import get_object_or_404, redirect, render
from cita.models import Cita
from inicio.views import login_required
from medico.forms import MedicoForm
from medico.models import Medico
from django.contrib.auth.models import User
from paciente.models import Paciente

# Create your views here.

def lista_medico(request):
    medico = Medico.objects.all() #select * from especialidades
    return render(request, 'medico/lista_medico.html', {'medico': medico})

def crear_medico(request):
    if request.method == 'POST': 
        form= MedicoForm(request.POST)
        if form.is_valid(): 
            medico = form.save()
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['correo_electronico'],
                password=request.POST['password'],
            )
            medico.user_id = user
            medico.save() 
            return redirect("lista_medico")
        else:
            return render(request, 'medico/crear_medico.html', {'form': form})
    else:
        form = MedicoForm()
        return render(request, 'medico/crear_medico.html', {'form': form})

def editar_medico(request, medico_id):
    medico=get_object_or_404(Medico, id=medico_id)
    if request.method ==  'POST':
        form= MedicoForm(request.POST,  instance=medico)

        if form.is_valid(): 
            form.save()
            return redirect("lista_medico")
        else:
            return render(request, 'medico/crear_medico.html', {'form': form})
    else:
        form = MedicoForm(instance=medico)
        return render(request, 'medico/crear_medico.html', {'form': form})

def eliminar_medico(request, medico_id):
    medico=get_object_or_404(Medico, id=medico_id)
    if request.method ==  'POST':
        medico.delete()
        return redirect("lista_medico")
    else:
        return render(request, 'medico/eliminar_medico.html', {'medico': medico})
    
@login_required    
def dashboard_medico(request):
    # Obtener el total de médicos activos e inactivos
    total_medicos_activos = Medico.objects.filter(estado="Activo").count()
    total_medicos_inactivos = Medico.objects.filter(estado="Dado de baja").count()

    # Obtener el total de pacientes con y sin COVID
    total_pacientes_covid = Cita.objects.filter(estado_covid="s").count()
    total_pacientes_no_covid = Cita.objects.filter(estado_covid="n").count()

    # Obtener otros contadores
    contador_pacientes = Paciente.objects.count()
    contador_citas = Cita.objects.count()

    # Crear el contexto combinado
    context = {
        'section': 'dashboard_medico',
        'total_medicos_activos': total_medicos_activos,
        'total_medicos_inactivos': total_medicos_inactivos,
        'total_pacientes_covid': total_pacientes_covid,
        'total_pacientes_no_covid': total_pacientes_no_covid,
        'contador_pacientes': contador_pacientes,
        'contador_citas': contador_citas,
    }

    # Renderizar la plantilla con el contexto
    return render(request, 'medico/dashboard_medico.html', context)




    


