from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from calendarioDisponibilidad.forms import CalendarioDisponibilidadForm, RangoDisponibilidadForm
from calendarioDisponibilidad.models import CalendarioDisponibilidad
from medico.models import Medico
from datetime import timedelta
from django.http import JsonResponse
from especialidades.models import Especialidades

# Lista de disponibilidades
def lista_calendarioDisponibilidad(request):
    calendarioDisponibilidad = CalendarioDisponibilidad.objects.all()  # select * from especialidades
    return render(request, 'calendarioDisponibilidad/lista_calendarioDisponibilidad.html', {'calendarioDisponibilidad': calendarioDisponibilidad})

# Crear una disponibilidad específica
def crear_calendarioDisponibilidad(request):
    if request.method == 'POST': 
        form = CalendarioDisponibilidadForm(request.POST)
        if form.is_valid(): 
            medico = form.cleaned_data['medico']
            
            # Verificar si el médico está activo
            if medico.estado != 'Activo':
                messages.error(request, 'No se puede crear disponibilidad para un médico que no está activo.')
                return redirect("crear_calendarioDisponibilidad")
            
            print('GUARDANDO DISPOBILIDAD...')
            
            form.save()
            messages.success(request, 'Disponibilidad creada exitosamente.')
            return redirect("lista_calendarioDisponibilidad")
        else:
            return render(request, 'calendarioDisponibilidad/crear_calendarioDisponibilidad.html', {'form': form})
    else:
        form = CalendarioDisponibilidadForm()
        return render(request, 'calendarioDisponibilidad/crear_calendarioDisponibilidad.html', {'form': form})

# Editar una disponibilidad específica
def editar_calendarioDisponibilidad(request, calendarioDisponibilidad_id):
    calendarioDisponibilidad = get_object_or_404(CalendarioDisponibilidad, id=calendarioDisponibilidad_id)
    if request.method == 'POST':
        form = CalendarioDisponibilidadForm(request.POST, instance=calendarioDisponibilidad)

        if form.is_valid():
            medico = form.cleaned_data['medico']
            
            # Verificar si el médico está activo
            if medico.estado != 'Activo':
                messages.error(request, 'No se puede modificar disponibilidad para un médico que no está activo.')
                return redirect("editar_calendarioDisponibilidad", calendarioDisponibilidad_id=calendarioDisponibilidad_id)
            
            form.save()
            messages.success(request, 'Disponibilidad actualizada exitosamente.')
            return redirect("lista_calendarioDisponibilidad")
        else:
            return render(request, 'calendarioDisponibilidad/crear_calendarioDisponibilidad.html', {'form': form})
    else:
        form = CalendarioDisponibilidadForm(instance=calendarioDisponibilidad)
        return render(request, 'calendarioDisponibilidad/crear_calendarioDisponibilidad.html', {'form': form})

# Eliminar una disponibilidad
def eliminar_calendarioDisponibilidad(request, calendarioDisponibilidad_id):
    calendarioDisponibilidad = get_object_or_404(CalendarioDisponibilidad, id=calendarioDisponibilidad_id)
    if request.method == 'POST':
        calendarioDisponibilidad.delete()
        messages.success(request, 'Disponibilidad eliminada exitosamente.')
        return redirect("lista_calendarioDisponibilidad")
    else:
        return render(request, 'calendarioDisponibilidad/eliminar_calendarioDisponibilidad.html', {'calendarioDisponibilidad': calendarioDisponibilidad})

def obtener_medicos(request):
    id_especialidad = request.GET.get('especialidad')
    fecha = request.GET.get('fecha')

    # Obtener la especialidad por su nombre
    try:
        especialidad = Especialidades.objects.get(id=id_especialidad)
    except Especialidades.DoesNotExist:
        return JsonResponse({'error': 'Especialidad no encontrada'}, status=400)

    # Filtrar médicos por la especialidad y fecha de disponibilidad
    if fecha is not None:
        medicos = Medico.objects.filter(especialidad__id=id_especialidad)
    else:
        medicos = Medico.objects.filter(especialidad__id=id_especialidad, calendariodisponibilidad__fecha_disponibilidad=fecha)
        
    print(medicos)

    # Convertimos los datos de los médicos en una lista para JSON
    medicos_data = [{'id': medico.id, 'nombre': str(medico)} for medico in medicos]

    return JsonResponse({'medicos': medicos_data})
