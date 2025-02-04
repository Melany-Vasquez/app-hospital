from . import views
from django.urls import path

urlpatterns = [
    path("", views.lista_historialMedico, name="lista_historialMedico"),
    path("insertar", views.crear_historialMedico, name="crear_historialMedico"),
    path("editar/<int:historialMedico_id>",  views.editar_historialMedico, name="editar_historialMedico"),
    path("eliminar/<int:historialMedico_id>", views.eliminar_historialMedico, name="eliminar_historialMedico"),
]