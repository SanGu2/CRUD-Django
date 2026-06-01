# Projeto: CRUD de Funcionários
# Integrantes: Augusto Lothar, Gustavo Pereira, Julio Lima, Rodrigo Córdova
# Data: 31/05/2026


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from datetime import datetime
from .models import Funcionario
from mongoengine.errors import DoesNotExist, InvalidQueryError

def listar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/list.html', {'funcionarios': funcionarios})

def adicionar_funcionario(request):
    if request.method == 'POST':
        try:
            salario = float(request.POST.get('salario'))
            data_admissao = datetime.strptime(request.POST.get('data_admissao'), '%Y-%m-%d').date()
            
            Funcionario(
                nome=request.POST['nome'].strip(),
                cargo=request.POST['cargo'].strip(),
                salario=salario,
                data_admissao=data_admissao
            ).save()
            return redirect('listar_funcionarios')
        except (ValueError, KeyError) as e:
            return HttpResponseBadRequest(f"Dados inválidos: {e}")
    return render(request, 'funcionario/form.html', {'action': 'create'})

def atualizar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, id=pk)
    try:
        # MongoEngine aceita string hex e converte para ObjectId internamente
        funcionario = Funcionario.objects.get(id=pk)
    except (DoesNotExist, InvalidQueryError):
        # Se não encontrar ou ID inválido, redireciona
        return redirect('listar_funcionarios')
    
    if request.method == 'POST':
        # ... lógica de atualização ...
        funcionario.save()
        return redirect('listar_funcionarios')
    
    return render(request, 'funcionario/form.html', {'funcionario': funcionario})

def remover_funcionario(request, pk):
    """Remove um funcionário pelo ID (ObjectId do MongoDB)"""
    if request.method != 'POST':
        # Segurança: só permite DELETE via POST
        return redirect('listar_funcionarios')
    
    try:
        # ✅ Busca nativa do MongoEngine (não usa get_object_or_404)
        funcionario = Funcionario.objects.get(id=pk)
        funcionario.delete()
    except (DoesNotExist, InvalidQueryError):
        # Se não encontrar ou ID inválido, apenas redireciona
        pass
    except Exception as e:
        # Opcional: logar erro para debug
        print(f"Erro ao remover: {e}")
    
    return redirect('listar_funcionarios')