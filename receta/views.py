from django.shortcuts import get_object_or_404, redirect, render
import inicio.views
import receta
from receta.models import Receta
from receta.forms import RecetaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
# Create your views here.
@login_required


def lista_receta(request):
    tipo_usuario = request.session.get('tipo_usuario')

    if not tipo_usuario:
        return HttpResponse("No autorizado", status=403)

    if tipo_usuario == 'Admin':
        receta = Receta.objects.all()  # Admin ve todas las recetas
        return render(request, 'receta/lista_receta.html', {'receta': receta})

    if tipo_usuario == 'Medico':
        id_medico = request.session.get('id_medico')
        receta = Receta.objects.filter(diagnostico__cita__medico_id=id_medico)
        return render(request, 'receta/lista_receta_medico.html', {'receta': receta})

    return HttpResponse("Tipo de usuario no válido", status=400)
    

@login_required
def crear_receta(request):
    if request.method == 'POST': 
        form= RecetaForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("lista_receta")
        else:
            return render(request, 'receta/crear_receta.html', {'form': form})
    else:
        form = RecetaForm()
        return render(request, 'receta/crear_receta.html', {'form': form})

@login_required   
def editar_receta(request, receta_id):
    receta=get_object_or_404(Receta, id=receta_id)
    if request.method ==  'POST':
        form= RecetaForm(request.POST,  instance=receta)

        if form.is_valid(): 
            form.save()
            return redirect("lista_receta")
        else:
            return render(request, 'receta/crear_receta.html', {'form': form})
    else:
        form = RecetaForm(instance=receta)
        return render(request, 'receta/crear_receta.html', {'form': form})

@login_required
def eliminar_receta(request, receta_id):
    receta=get_object_or_404(Receta, id=receta_id)
    if request.method ==  'POST':
        receta.delete()
        return redirect("lista_receta")
    else:
        return render(request, 'receta/eliminar_receta.html', {'receta': receta})

def crear_receta_medico(request):
    if request.method == 'POST': 
        form = RecetaForm(request.POST, request=request)  # Pasar request al formulario
        if form.is_valid(): 
            form.save()
            return redirect("lista_receta_medico")
    else:
        form = RecetaForm(request=request)  # Pasar request al formulario

    return render(request, 'receta/crear_receta_medico.html', {'form': form})
 