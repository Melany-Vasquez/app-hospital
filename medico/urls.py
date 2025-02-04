
from django.urls import path
from medico.views import dashboard_medico
from . import views


urlpatterns = [
    path("", views.lista_medico, name="lista_medico"),
    path("insertar", views.crear_medico, name="crear_medico"),
    path("editar/<int:medico_id>",  views.editar_medico, name="editar_medico"),
    path("eliminar/<int:medico_id>", views.eliminar_medico, name="eliminar_medico"),
    path("dashboard", views.dashboard_medico, name="dashboard_medico")
    
    
    
    
]