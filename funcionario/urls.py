from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_funcionarios, name='listar_funcionarios'),
    path('adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('atualizar/<str:pk>/', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('remover/<str:pk>/', views.remover_funcionario, name='remover_funcionario'),
]