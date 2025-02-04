from django.urls import path
from . import views

urlpatterns = [
    #gestion habilitada solo de admin
    path("", views.lista_cita, name="lista_cita"),
    path("insertar", views.crear_cita, name="crear_cita"),
    path("editar/<int:citas_id>",  views.editar_cita, name="editar_cita"),
    path("eliminar/<int:citas_id>", views.eliminar_cita, name="eliminar_cita"),
    
    #gestion habilitada solo de medico
    path("medico/insertar/cita", views.crear_cita_medico, name="crear_cita_medico"),
    path("medico/editar/cita/<int:citas_id>",  views.editar_cita_medico, name="editar_cita_medico"),
    path("medico/lista/cita/",  views.lista_cita_medico, name="lista_citas_medico"),
    path("eliminar/<int:citas_id>", views.eliminar_cita_medico, name="eliminar_cita_medico"),
    
    path("medico/lista/cita/",  views.lista_cita_paciente, name="lista_citas_paciente"),
    path("paciente/insertar/cita", views.crear_cita_paciente, name="crear_citas_paciente"),
    path("eliminar/<int:citas_id>", views.eliminar_cita_paciente, name="eliminar_cita_paciente"),
    path("paciente/editar/<int:citas_id>",  views.editar_cita_paciente, name="editar_cita_paciente"),
]