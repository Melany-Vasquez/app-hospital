import cita
from django.shortcuts import redirect, render

from roles_user.forms import RolForm
from calendarioDisponibilidad.forms import RangoDisponibilidadForm

# Create your views here.
def crear_user(request):
    if request.method == 'POST': 
        form= RolForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("#")
        else:
            return render(request, '#', {'form': form})
    else:
        form = RolForm()
        return render(request, 'roles_usuario/crear_user.html', {'form': form})
    
    