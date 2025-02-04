from django.shortcuts import get_object_or_404, redirect, render
from historialMedico.forms import historialMedicoForm
from historialMedico.models import HistorialMedico
from inicio.views import login_required

# Create your views here.
@login_required                                                      
def lista_historialMedico(request):
    historialMedico = HistorialMedico.objects.all() #select * from especialidades
    return render(request, 'historialMedico/lista_historialMedico.html', {'historialMedico': historialMedico})

@login_required
def crear_historialMedico(request):
    if request.method == 'POST': 
        form= historialMedicoForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("historialMedico")
        else:
            return render(request, 'historialMedico/crear_historialMedico.html', {'form': form})
    else:
        form = historialMedicoForm()
        return render(request, 'historialMedico/crear_historialMedico.html', {'form': form})

@login_required
def editar_historialMedico(request, historialMedico_id):
    historialMedico=get_object_or_404(HistorialMedico, id=historialMedico_id)
    if request.method ==  'POST':
        form= historialMedicoForm(request.POST,  instance=historialMedico)

        if form.is_valid(): 
            form.save()
            return redirect("lista_historialMedico")
        else:
            return render(request, 'historialMedico/crear_historialMedico.html', {'form': form})
    else:
        form = historialMedicoForm(instance=historialMedico)
        return render(request, 'historialMedico/crear_historialMedico.html', {'form': form})

@login_required
def eliminar_historialMedico(request, historialMedico_id):
    historialMedico=get_object_or_404(HistorialMedico, id=historialMedico_id)
    if request.method ==  'POST':
        historialMedico.delete()
        return redirect("lista_historialMedico")
    else:
        return render(request, 'historialMedico/eliminar_historialMedico.html', {'historialMedico': historialMedico})
    
    
        