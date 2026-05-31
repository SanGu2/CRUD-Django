# Projeto: CRUD de Funcionários
# Integrantes: Augusto Lothar, Gustavo Pereira, Julio Lima, Rodrigo Córdova
# Data: 31/05/2026

from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'salario', 'data_admissao']
    search_fields = ['nome', 'cargo']
    list_filter = ['cargo', 'data_admissao']

