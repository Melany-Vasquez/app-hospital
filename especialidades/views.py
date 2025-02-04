from django.shortcuts import redirect, render,  get_object_or_404
from especialidades.models import Especialidades
from especialidades.forms import EspecialidadesForm
from inicio.views import login_required

# Create your views here.
@login_required
def lista_especialidades(request):
    especialidades = Especialidades.objects.all() #select * from especialidades
    return render(request, 'especialidades/lista_especialidades.html', {'especialidades': especialidades})

@login_required
def crear_especialidades(request):
    if request.method == 'POST': 
        form= EspecialidadesForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("lista_especialidades")
        else:
            return render(request, 'especialidades/crear_especialidades.html', {'form': form})
    else:
        form = EspecialidadesForm()
        return render(request, 'especialidades/crear_especialidades.html', {'form': form})

@login_required
def editar_especialidades(request, especialidad_id):
    especialidad=get_object_or_404(Especialidades, id=especialidad_id)
    if request.method ==  'POST':
        form= EspecialidadesForm(request.POST,  instance=especialidad)

        if form.is_valid(): 
            form.save()
            return redirect("lista_especialidades")
        else:
            return render(request, 'especialidades/crear_especialidades.html', {'form': form})
    else:
        form = EspecialidadesForm(instance=especialidad)
        return render(request, 'especialidades/crear_especialidades.html', {'form': form})

@login_required
def eliminar_especialidades(request, especialidad_id):
    especialidad=get_object_or_404(Especialidades, id=especialidad_id)
    if request.method ==  'POST':
        especialidad.delete()
        return redirect("lista_especialidades")
    else:
        return render(request, 'especialidades/eliminar_especialidades.html', {'especialidad': especialidad})
