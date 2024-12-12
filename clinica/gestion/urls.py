from django.urls import path
from . import views

urlpatterns = [

    path('index.html', views.index, name='index'),
    path('doctores.html', views.doctores, name='doctores'),
    path('pacientesCitas.html', views.pacientes, name='pacientes'), 
]