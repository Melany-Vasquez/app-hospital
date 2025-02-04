from django.urls import path
from . import views


urlpatterns = [
    path("", views.lista_calendarioDisponibilidad, name="lista_calendarioDisponibilidad"),
    path("insertar", views.crear_calendarioDisponibilidad, name="crear_calendarioDisponibilidad"),
    path("editar/<int:calendarioDisponibilidad_id>",  views.editar_calendarioDisponibilidad, name="editar_calendarioDisponibilidad"),
    path("eliminar/<int:calendarioDisponibilidad_id>", views.eliminar_calendarioDisponibilidad, name="eliminar_calendarioDisponibilidad"),
    path("filtro_especialidad", views.obtener_medicos, name ="filtro_especialidad"),
]