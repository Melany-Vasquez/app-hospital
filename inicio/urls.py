from django.urls import path
from . import views  # Importar las vistas desde el mismo directorio

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta de la página de inicio
    path('crearcuenta', views.crearcuenta, name='crearcuenta'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion' ), 
    path('cerrarsesion', views.signout, name='cerrarsesion' ),             
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("dashboard_admin", views.dashboard_admin, name="dashboard_admin"),
                      
]