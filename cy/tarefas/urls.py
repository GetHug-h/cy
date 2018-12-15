from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tarefas/', views.tarefa_list, name='tarefa-list'),
    path('tarefas/<int:pk>', views.tarefa_detail, name='tarefa-detail'),
    path('entradas/', views.input_list, name='entrada-list'),
    path('entradas/<int:pk>', views.input_detail, name='entrada-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
