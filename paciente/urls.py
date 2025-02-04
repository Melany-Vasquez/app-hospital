from django.urls import path  
from . import views

urlpatterns = [
    path("", views.lista_paciente, name="lista_paciente"),
    path("insertar", views.crear_paciente, name="crear_paciente"),
    path("editar/<int:paciente_id>",  views.editar_paciente, name="editar_paciente"),
    path("eliminar/<int:paciente_id>", views.eliminar_paciente, name="eliminar_paciente"), 
    path("dashboard_paciente", views.dashboard_paciente, name="dashboard_paciente"),
    
    #gestion habilitada solo de medico
    path("medico/insertar/paciente", views.crear_paciente_medico, name="crear_paciente_medico"),
    path("medico/lista/paciente/",  views.lista_paciente_medico, name="lista_paciente_medico"),
    path("editar/medico/<int:paciente_id>",  views.editar_paciente_medico, name="editar_paciente_medico"),
    path("eliminar/medico/<int:paciente_id>", views.eliminar_paciente_medico, name="eliminar_paciente_medico"), 
    
    #gestion habilitada solo de paciente
    path("editar/paciente/<int:paciente_id>",  views.editar_paciente_usuario, name="editar_paciente_usuario"),
    
    
]