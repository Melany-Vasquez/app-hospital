from django.urls import path  
from . import views

urlpatterns = [
    path("", views.lista_receta, name="lista_receta"),
    path("insertar", views.crear_receta, name="crear_receta"),
    path("editar/<int:receta_id>",  views.editar_receta, name="editar_receta"),
    path("eliminar/<int:receta_id>", views.eliminar_receta, name="eliminar_receta"),
    
    #gestion habilitada solo de medico
    path("medico/insertar/receta", views.crear_receta_medico, name="crear_receta_medico"),
    path("medico/lista/receta",  views.lista_receta, name="lista_receta_medico"),
    
]