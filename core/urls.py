from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.lista_medicos, name='lista_medicos'),
    path('medicos/novo/', views.cadastrar_medico, name='cadastrar_medico'),
]
