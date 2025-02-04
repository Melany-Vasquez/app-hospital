from django.contrib import messages
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from cita.models import Cita
from inicio.views import login_required
from medico.models import Medico
from paciente.models import Paciente
from paciente.forms import PacienteForm
from django.contrib.auth.models import User

# Create your views here.


def lista_paciente(request):
    paciente = Paciente.objects.all()
    tipo_usuario = request.session['tipo_usuario'] #select * from especialidades
    
    if(tipo_usuario == 'Admin'):
        paciente = Paciente.objects.all() #select * from especialidades
        return render(request, 'paciente/lista_paciente.html', {'paciente': paciente})
    
    if(tipo_usuario == 'Medico'):
        id_medico = request.session['id_medico']
        return render(request, 'paciente/lista_paciente_medico.html', {'paciente': paciente})


def crear_paciente(request):
    if request.method == 'POST': 
        form= PacienteForm(request.POST)
        if form.is_valid(): 
            paciente = form.save()
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['correo_electronico'],
                password=request.POST['password'],
            )
            paciente.user_id = user
            paciente.save() 
            return redirect("lista_paciente")
        else:
            return render(request, 'paciente/crear_paciente.html', {'form': form})
    else:
        form = PacienteForm()
        return render(request, 'paciente/crear_paciente.html', {'form': form})
    

def editar_paciente(request, paciente_id):
    paciente=get_object_or_404(Paciente, id=paciente_id)
    has_user = False
    user = {
        'username': '',
        'password': '',
        'email': ''
    }
    if(paciente.user_id):
        has_user = True
        user = User.objects.get(id=paciente.user_id.id)
    if request.method ==  'POST':
        form= PacienteForm (request.POST,  instance=paciente)

        if form.is_valid(): 
            if(has_user):
                user.username = request.POST['username']
                user.email = request.POST['correo_electronico']
                if request.POST['password']:
                    user.set_password(request.POST['password']) 
                user.save()
                form.save()
            else:
                paciente = form.save()
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['correo_electronico'],
                    password=request.POST['password'],
                )
                paciente.user_id = user
                paciente.save() 
            return redirect("lista_paciente")
        else:
            return render(request, 'paciente/crear_paciente.html', {'form': form, 'user': user})
    else:
        form = PacienteForm(instance=paciente)
        return render(request, 'paciente/crear_paciente.html', {'form': form, 'user': user})

def editar_paciente_medico(request, paciente_id):
    paciente=get_object_or_404(Paciente, id=paciente_id)
    has_user = False
    user = {
        'username': '',
        'password': '',
        'email': ''
    }
    if(paciente.user_id):
        has_user = True
        user = User.objects.get(id=paciente.user_id.id)
    if request.method ==  'POST':
        form= PacienteForm (request.POST,  instance=paciente)

        if form.is_valid(): 
            if(has_user):
                user.username = request.POST['username']
                user.email = request.POST['correo_electronico']
                if request.POST['password']:
                    user.set_password(request.POST['password']) 
                user.save()
                form.save()
            else:
                paciente = form.save()
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['correo_electronico'],
                    password=request.POST['password'],
                )
                paciente.user_id = user
                paciente.save() 
            return redirect("lista_paciente_medico")
        else:
            return render(request, 'paciente/crear_paciente_medico.html', {'form': form, 'user': user})
    else:
        form = PacienteForm(instance=paciente)
        return render(request, 'paciente/crear_paciente_medico.html', {'form': form, 'user': user})


def eliminar_paciente(request, paciente_id):
    paciente=get_object_or_404(Paciente, id=paciente_id)
    if request.method ==  'POST':
        paciente.delete()
        return redirect("lista_paciente")
    else:
        return render(request, 'paciente/eliminar_paciente.html', {'paciente': paciente})

def eliminar_paciente_medico(request, paciente_id):
    paciente=get_object_or_404(Paciente, id=paciente_id)
    if request.method ==  'POST':
        paciente.delete()
        return redirect("lista_paciente")
    else:
        return render(request, 'paciente/eliminar_paciente_medico.html', {'paciente': paciente})
    
def crear_paciente_medico(request):
    if request.method == 'POST': 
        form= PacienteForm(request.POST)
        if form.is_valid(): 
            paciente = form.save()
            user = User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['correo_electronico'],
                password=request.POST['password'],
            )
            paciente.user_id = user
            paciente.save() 
            return redirect("lista_paciente_medico")
        else:
            return render(request, 'paciente/crear_paciente_medico.html', {'form': form})
    else:
        form = PacienteForm()
        return render(request, 'paciente/crear_paciente_medico.html', {'form': form})
    
@login_required   
def dashboard_paciente(request):
    # Obtener el total de médicos activos e inactivos

    return render(request, 'paciente/dashboard_paciente.html')

    paciente = Paciente.objects.get(user=request.user)  # Obtener el paciente del usuario logueado
    return render(request, 'dashboard_paciente.html', {
        'paciente': paciente,
        'username': request.user.username  # Pasa el nombre de usuario al contexto
    })
    
def editar_paciente_usuario(request, paciente_id):
    paciente=get_object_or_404(Paciente, id=paciente_id)
    has_user = False
    user = {
        'username': '',
        'password': '',
        'email': ''
    }
    if(paciente.user_id):
        has_user = True
        user = User.objects.get(id=paciente.user_id.id)
    if request.method ==  'POST':
        form= PacienteForm (request.POST,  instance=paciente)

        if form.is_valid(): 
            if(has_user):
                user.username = request.POST['username']
                user.email = request.POST['correo_electronico']
                if request.POST['password']:
                    user.set_password(request.POST['password']) 
                user.save()
                form.save()
            else:
                paciente = form.save()
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['correo_electronico'],
                    password=request.POST['password'],
                )
                paciente.user_id = user
                paciente.save() 
            return redirect("lista_paciente")
        else:
            return render(request, 'paciente/editar_paciente_usuario.html', {'form': form, 'user': user})
    else:
        form = PacienteForm(instance=paciente)
        return render(request, 'paciente/editar_paciente_usuario.html', {'form': form, 'user': user})


def lista_paciente_medico(request):
    paciente = Paciente.objects.all()
    tipo_usuario = request.session['tipo_usuario'] #select * from especialidades
    
    if(tipo_usuario == 'Admin'):
        paciente = Paciente.objects.all() #select * from especialidades
        return render(request, 'paciente/lista_paciente.html', {'paciente': paciente})
    
    if(tipo_usuario == 'Medico'):
        id_medico = request.session['id_medico']
        return render(request, 'paciente/lista_paciente_medico.html', {'paciente': paciente})    