from django.urls import path
from . import views

urlpatterns = [
    path('reporte_citas/', views.reporte_citas, name='reporte_citas'),
]