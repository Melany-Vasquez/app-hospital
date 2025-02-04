
from django.urls import path
from diagnostico.views import lista_diagnostico
from . import views


urlpatterns = [
    
    path("", views.lista_diagnostico, name="lista_diagnostico"),
    path("insertar", views.crear_diagnostico, name="crear_diagnostico"),
    path("editar/<int:diagnostico_id>",  views.editar_diagnostico, name="editar_diagnostico"),
    path("eliminar/<int:diagnostico_id>", views.eliminar_diagnostico, name="eliminar_diagnostico"),
    
    #gestion habilitada solo para paciente
    path("paciente/diagnosticos", views.lista_diagnostico, name="lista_diagnostico_paciente"),
    
    #gestion habilitada solo de medico
    path("medico/insertar/diagnostico", views.crear_diagnostico_medico, name="crear_diagnostico_medico"),
    path("medico/lista/diagnostico", views.lista_diagnostico_medico, name="lista_diagnostico_medico"),
    path("medico/editar/diagnostico", views.editar_diagnostico, name="editar_diagnostico_medico"),
]