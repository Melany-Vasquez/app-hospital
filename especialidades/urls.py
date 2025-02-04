
from django.urls import path  
from . import views

urlpatterns = [
    path("", views.lista_especialidades, name="lista_especialidades"),
    path("insertar", views.crear_especialidades, name="crear_especialidades"),
    path("editar/<int:especialidad_id>",  views.editar_especialidades, name="editar_especialidades"),
    path("eliminar/<int:especialidad_id>", views.eliminar_especialidades, name="eliminar_especialidades"),
]