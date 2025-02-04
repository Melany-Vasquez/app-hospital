

# Create your views here.
from especialidades.models import Especialidades
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
import cita
from cita.forms import CitaForm, CitaForm_medico, CitaForm_paciente
from cita.models import Cita
from inicio.views import login_required_and_check_session

# Create your views here.


# Aui enlisto todas las itas y se presenta según ID 

def lista_cita(request):
    tipo_usuario = request.session['tipo_usuario'] 
    
    if(tipo_usuario == 'Admin'):
        citas = Cita.objects.all() #select * from especialidades
        return render(request, 'citas/lista_citas.html', {'citas': citas})
    
    if(tipo_usuario == 'Paciente'):
        id_paciente = request.session['id_paciente']
        citas = Cita.objects.filter(paciente_id = id_paciente) 
        return render(request, 'citas/lista_cita_paciente.html', {'citas': citas})
    
    if(tipo_usuario == 'Medico'):
        id_medico = request.session['id_medico']
        citas = Cita.objects.filter(medico_id = id_medico) 
        return render(request, 'citas/lista_citas_medico.html', {'citas': citas})


def lista_cita_paciente(request):
    tipo_usuario = request.session['tipo_usuario'] 
    
    if(tipo_usuario == 'Admin'):
        citas = Cita.objects.all() #select * from especialidades
        return render(request, 'citas/lista_citas.html', {'citas': citas})
    
    if(tipo_usuario == 'Paciente'):
        id_paciente = request.session['id_paciente']
        citas = Cita.objects.filter(paciente_id = id_paciente) 
        return render(request, 'citas/lista_cita_paciente.html', {'citas': citas})
    
    if(tipo_usuario == 'Medico'):
        id_medico = request.session['id_medico']
        citas = Cita.objects.filter(medico_id = id_medico) 
        return render(request, 'citas/lista_citas_medico.html', {'citas': citas})

def lista_cita_medico(request):
    tipo_usuario = request.session['tipo_usuario'] 
    
    if(tipo_usuario == 'Admin'):
        citas = Cita.objects.all() #select * from especialidades
        return render(request, 'citas/lista_citas.html', {'citas': citas})
    
    if(tipo_usuario == 'Paciente'):
        id_paciente = request.session['id_paciente']
        citas = Cita.objects.filter(paciente_id = id_paciente) 
        return render(request, 'citas/lista_cita_paciente.html', {'citas': citas})
    
    if(tipo_usuario == 'Medico'):
        id_medico = request.session['id_medico']
        citas = Cita.objects.filter(medico_id = id_medico) 
        return render(request, 'citas/lista_citas_medico.html', {'citas': citas})

def crear_cita(request):
    if request.method == 'POST': 
        form= CitaForm(request.POST)
        print(form)
        #consultar a la tabla medico la fecha de inicio y fin que este dentro de la fecha del formulario y valido. get filtrado modelo
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas.html', {'form': form})
    else:
        form = CitaForm()
        return render(request, 'citas/crear_citas.html', {'form': form})

 
def editar_cita(request, citas_id):
    print('CREAR CITA FORM...')
    citas =get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        form= CitaForm(request.POST,  instance= citas)
        print(form.is_valid())
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas.html', {'form': form})
    else:
        form = CitaForm( instance = citas)
        return render(request, 'citas/crear_citas.html', {'form': form})

def editar_cita_medico(request, citas_id):
    print('CREAR CITA FORM...')
    citas =get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        form= CitaForm(request.POST,  instance= citas)
        print(form.is_valid())
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas_medico.html', {'form': form})
    else:
        form = CitaForm( instance = citas)
        return render(request, 'citas/crear_citas_medico.html', {'form': form})
    
def editar_cita_paciente(request, citas_id):
    print('CREAR CITA FORM...')
    citas =get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        form= CitaForm(request.POST,  instance= citas)
        print(form.is_valid())
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas_paciente.html', {'form': form})
    else:
        form = CitaForm( instance = citas)
        return render(request, 'citas/crear_citas_paciente.html', {'form': form})
        
def eliminar_cita (request, citas_id):
    citas=get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        citas.delete()
        return redirect("lista_cita")
    else:
        return render(request, 'citas/eliminar_citas.html', {'citas': citas})
    
def eliminar_cita_paciente (request, citas_id):
    citas=get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        citas.delete()
        return redirect("lista_citas_paciente")
    else:
        return render(request, 'citas/eliminar_cita_paciente.html', {'citas': citas})   
    
def eliminar_cita_medico (request, citas_id):
    citas=get_object_or_404(Cita, id=citas_id)
    if request.method ==  'POST':
        citas.delete()
        return redirect("lista_citas_medico")
    else:
        return render(request, 'citas/eliminar_cita_medico.html', {'citas': citas})     
    
def getIdMedico(request):
    return request.session.id_medico 



def crear_cita_medico(request):
    if request.method == 'POST': 
        form= CitaForm_medico(request.POST)
        print(form)
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas_medico.html', {'form': form})
    else:
        form = CitaForm_medico(
            id_medico = request.session['id_medico']
        )
        return render(request, 'citas/crear_citas_medico.html', {'form': form})


def crear_cita_paciente(request):
    if request.method == 'POST': 
        form= CitaForm_paciente(request.POST)
        print(form)
        if form.is_valid(): 
            form.save()
            return redirect("lista_cita")
        else:
            return render(request, 'citas/crear_citas_paciente.html', {'form': form})
    else:
        form = CitaForm_paciente(
            id_paciente = request.session['id_paciente']
        )
        return render(request, 'citas/crear_citas_paciente.html', {'form': form})
      